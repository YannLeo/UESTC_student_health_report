import time
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import evening
import morning
import json

def getINFO(path_config):
    with open(path_config) as f:
        info = json.load(f)
    return info

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    for root, dirs, files in os.walk('/home/yl/CodeAndData/UESTC_student_health_report/config'):
        for f in files:
            info = getINFO(root + '/' + f)
            # print(f, info)
            time_morning = info['time']['morning']
            time_evening = info['time']['evening']
            scheduler.add_job(morning.morning, 'cron', hour=time_morning['hour'], minute=time_morning['minute'], args=[info])
            scheduler.add_job(evening.evening, 'cron', hour=time_evening['hour'], minute=time_evening['minute'], args=[info])
    scheduler.start()