# cofing: utf-8
import schedule
import time
import datetime
import smbus
import bme280

bus_number = 1
i2c_address = 0x76

bus = smbus.SMBus(bus_number)

digT = []
digP = []
digH = []

t_fine = 0.0

bme280.setup(bus)
bme280.get_calib_param()

def job():
    sensor["Temperature"], sensor["Pressure"], sensor["Humidity"] = bme280.readdata()
    print(datetime.datetime.now())
    print(sensor["Temperature"])

schedule.every().minutes.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
