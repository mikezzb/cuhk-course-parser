import requests
from PIL import Image
from bs4 import BeautifulSoup
from contextlib import closing
import io

class Course:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
        self.form_headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.course_url = 'http://rgsntl.rgs.cuhk.edu.hk/aqs_prd_applx/Public/tt_dsp_crse_catalog.aspx'
        self.sess = requests.Session()
        self.courses = {}

    def get_code_list(self):
        with closing(requests.get(self.course_url, headers=self.headers)) as res:
            soup = BeautifulSoup(res.text, 'html.parser')
            code_list = []
            for node in soup.select('option'):
                code_list.append(node.text)
            self.code_list = list(filter(None, code_list))

    def get_captcha(self, url, manual=True):
        with closing(self.sess.get(url, headers=self.headers)) as captcha_res:
            in_memory_file = io.BytesIO(captcha_res.content)
            im = Image.open(in_memory_file)
            im.show()
            captcha = str(input('Input the captcha here: '))
            return captcha

    @staticmethod
    def get_form(soup: BeautifulSoup) -> dict:
        form_body = {'__VIEWSTATEFIELDCOUNT': soup.select_one('#__VIEWSTATEFIELDCOUNT')['value']}
        form_keys = ['__EVENTVALIDATION', '__VIEWSTATEGENERATOR', 'hf_Captcha', '__VIEWSTATE'] + [f"__VIEWSTATE{str(i)}" for i in range(1, int(form_body['__VIEWSTATEFIELDCOUNT']))]
        for k in form_keys:
            form_body[k] = soup.select_one(f'#{k}')['value']
        form_body.update({
            'btn_search': 'Search',
            'hf_previous_page': 'SEARCH',
            'hf_max_search_iteration': 1,
            'hf_search_iteration': 1,
        })
        return form_body

    def search_subject(self, subject):
        with closing(self.sess.get(self.course_url, headers=self.headers)) as res:
            soup = BeautifulSoup(res.text, 'html.parser')
            form_body = self.get_form(soup)
            captcha_node = soup.select_one('#imgCaptcha')
            captcha_url = f"http://rgsntl.rgs.cuhk.edu.hk/aqs_prd_applx/Public/{captcha_node['src']}"
            captcha = self.get_captcha(captcha_url)
            form_body.update({
                'txt_captcha': captcha,
                'ddl_subject': subject,
            })
            with closing(self.sess.post(self.course_url, headers=self.form_headers, data=form_body)) as res:
                self.parse_subject_courses(subject, res.text)
    
    def parse_subject_courses(self, subject, html):
        course_list = []
        soup = BeautifulSoup(html, 'html.parser')
        course_row_nodes = soup.select('.normalGridViewRowStyle') + soup.select('.normalGridViewAlternatingRowStyle')
        for row in course_row_nodes:
            a_node = row.select('a')
            course = {
                'code': a_node[0].text,
                'title': a_node[1].text,
                'id': a_node[1]['id'], # used to get details later
            }
            course_list.append(course)
        self.courses[subject] = sorted(course_list, key=lambda x:x['code'])

    def get_course_detail(self, form_body: dict, event_target: str):
        form_body.update({
            '__EVENTTARGET': event_target
            # sth like gv_detail$ctl02$lbtn_course_title, inside <a> of class normalGridViewAlternatingRowStyle and normalGridViewRowStyle
        })

cusis = Course()
cusis.get_code_list()
cusis.search_subject('CSCI')
print(cusis.courses)
