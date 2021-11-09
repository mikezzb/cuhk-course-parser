import os

def make_dirs(dirs):
    for dir in dirs:
        if not os.path.isdir(dir):
            os.mkdir(dir)

def parse_days_and_times(s: str) -> tuple:
    if s == 'TBA':
        return ('TBA', 'TBA', 'TBA')
    def to_24_hours(s: str):
        if 'PM' in s:
            s = s.replace('PM','')
            t = s.split(':')
            if t[0] != '12':
                t[0] = str(int(t[0])+12)
                s = ':'.join(t)
        else:
            s = s.replace('AM','')
        return s
    days_dict = {
        'Mo': 1,
        'Tu': 2,
        'We': 3,
        'Th': 4,
        'Fr': 5,
        'Sa': 6,
        'Su': 0,
    }
    raw = list(filter(lambda x: x!='-', s.split())) # first is 2-letter weekday abbr, second is start time, last is end time
    return (days_dict[raw[0]], to_24_hours(raw[1]), to_24_hours(raw[2]))
