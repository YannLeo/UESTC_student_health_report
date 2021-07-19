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
    scheduler.add_job(morning.morning, 'cron', hour=0, minute=10, args=[info])
    scheduler.add_job(evening.evening, 'cron', hour=17, minute=5, args=[info])
    scheduler.start()
    