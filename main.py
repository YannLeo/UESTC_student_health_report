import time
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import evening
import morning


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(morning.morning, 'cron', hour=0, minute=10)
    scheduler.add_job(evening.evening, 'cron', hour=17, minute=5)
    scheduler.start()
    