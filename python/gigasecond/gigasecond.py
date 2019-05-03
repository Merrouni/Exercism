import datetime

def add_gigasecond(moment):
    interval = datetime.timedelta(seconds=1000000000) 
    return moment + interval
