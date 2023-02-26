# CUHK Course Scraper
### Functions
* `search_subject`: Input desired subject code, e.g. ACCT, parser will save courses under ACCT in `dirname/courses/ACCT.json`.

* `parse_all`: Parses all subjects, and save courses in `[subject].json` for each subject.

### Examples

Run `demo.ipynb`
> E.g. Get all courses under a subject (e.g. AIST)
```python
cs = CourseScraper()
cs.search_subject(subject="AIST")
```
In `courses/AIST.json` (Selected)

```json
[
   {
      "code":"3020",
      "title":"Introduction to Computer Systems",
      "career":"Undergraduate",
      "units":"3.00",
      "grading":"Graded",
      "components":"Laboratory Lecture",
      "campus":"Main Campus",
      "academic_group":"Dept of Computer Sci & Engg",
      "requirements":"Prerequisite: (ENGG1110 or ESTR1002) AND (ENGG2440 or ESTR2004)",
      "description":"This course aims to provide students the basic knowledge of computer systems through the study of computer organization, assembly language and C programming. The course will mainly have two parts: (1) the structure of a computer that includes topics like data representations, digital logic structures, the Von Neumann model, assembly language, I/O, traps, subroutines and the stack; (2) system programming with C that includes topics like functions, pointers and arrays, file operations, dynamic memory management and data structures.",
      "outcome":"At the end of the course of studies, students will have acquired the ability to\r\u00a01. understand the underlying structure of a computer, the functions of its components, and the Von Neumann model;\u00a02. write simple assembly programs and understand how assembly programs works;\u00a03. develop system-level software with C.",
      "syllabus":"This course aims to provide students the basic knowledge of computer systems through the study of computer organization, assembly language and C programming. The course will mainly have two parts: (1) the structure of a computer that includes topics like data representations, digital logic structures, the Von Neumann model, assembly language, I/O, traps, subroutines and the stack; (2) system programming with C that includes topics like functions, pointers and arrays, file operations, dynamic memory management and data structures.",
      "required_readings":"1. Introduction to Computing Systems: From Bits and Gates to C and Beyond, Yale Patt and Sanjay Patel\r\u00a02. Computer systems: a programmer\u2019s perspective, Randal E. Bryant, David R. O\u2019Hallaron",
      "recommended_readings":"",
      "terms":{
         "2020-21 Term 2":{
            "--LEC (5034)":{
               "startTimes":[
                  "11:30",
                  "16:30"
               ],
               "endTimes":[
                  "12:15",
                  "18:15"
               ],
               "days":[
                  2,
                  3
               ],
               "locations":[
                  "Online Teaching",
                  "Online Teaching"
               ],
               "instructors":[
                  "Professor xxx",
                  "Professor xxx"
               ]
            },
            "-L01-LAB (5035)":{
               "startTimes":[
                  "16:30"
               ],
               "endTimes":[
                  "17:15"
               ],
               "days":[
                  2
               ],
               "locations":[
                  "Online Teaching"
               ],
               "instructors":[
                  "Professor xxx"
               ]
            }
         }
      },
      "assessments":{
         "Essay test or exam":"40",
         "Homework or assignment":"40",
         "Lab reports":"10",
         "Others":"10"
      }
   }
]
```

### Results (CUHK Course Data)

[cuhk-course-data](https://github.com/cutopia-labs/cuhk-course-data)
