# cofing: utf-8
import schedule
import time
import datetime
import bme280

t_fine = 0.0

bme280.setup()
bme280.get_calib_param()

sensor = {}

def job():
    sensor["Temperature"], sensor["Pressure"], sensor["Humidity"] = bme280.readdata()
    print(datetime.datetime.now())
    print(sensor["Temperature"])

schedule.every().minutes.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
