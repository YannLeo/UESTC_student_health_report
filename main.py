import time
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import evening
import morning
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default="config.json")

def getINFO():
    args = parser.parse_args()
    with open(args.config) as f:
        info = json.load(f)
    return info

if __name__ == '__main__':
    info = getINFO()
    scheduler = BlockingScheduler()
    time_morning = info['time']['morning']
    time_evening = info['time']['evening']
    scheduler.add_job(morning.morning, 'cron', hour=time_morning['hour'], minute=time_morning['minute'], args=[info])
    scheduler.add_job(evening.evening, 'cron', hour=time_evening['hour'], minute=time_evening['minute'], args=[info])
    scheduler.start()
    