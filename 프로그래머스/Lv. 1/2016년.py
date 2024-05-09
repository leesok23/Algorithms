import datetime

def solution(a, b):
    week_day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return week_day[datetime.datetime(2016,a,b).weekday()]
