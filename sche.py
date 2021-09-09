import schedule
import time
import datetime

def job():
    print(datetime.datetime.now())

schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
