# cofing: utf-8
import schedule
import time
import datetime
import bme280
import csv

t_fine = 0.0

bme280.setup()
bme280.get_calib_param()

sensor = {}

def job():
    sensor["Temperature"], sensor["Pressure"], sensor["Humidity"] = bme280.readdata()
    print(datetime.datetime.now())
    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.datetime.now(),sensor["Temperature"],sensor["Humidity"],sensor["Pressure"]])
    f.close()

schedule.every().minutes.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
