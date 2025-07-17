import time
import random
def randdate(sdate,edate):
    print("start and end dates are-",sdate,edate)
    rand=random.random()
    dateformate='%m/%d/%Y'
    startime=time.mktime(time.strptime(sdate,dateformate))
    endtime=time.mktime(time.strptime(edate,dateformate))
    randomtime=startime+rand*(endtime-startime)
    randomdate=time.strftime(dateformate,time.localtime(randomtime))
    return randomdate
print("random date is",randdate("6/13/2018","4/25/2025"))