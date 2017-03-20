import mraa
import time
from datetime import datetime as dt
import numpy as np

TRIG_PIN = 0
ECHO_PIN = 1

trig = mraa.Gpio(TRIG_PIN)
echo = mraa.Gpio(ECHO_PIN)

trig.dir(mraa.DIR_OUT)
echo.dir(mraa.DIR_IN)


def reject_outliers(data, m=2):
    return data[abs(data - np.mean(data)) < m * np.std(data)]


def pulse_in():
    pulse_on = dt.now()
    pulse_off = dt.now()
    while echo.read() == 0:
        print("wait 1")
        pulse_on = dt.now()
    while echo.read() == 1:
        print("wait 0")
        pulse_off = dt.now()
    return (pulse_off - pulse_on).microseconds


def has_obstacle():
    trig.write(1)
    time.sleep(0.00002)
    trig.write(0)
    return (17000 * pulse_in() * 0.000001) < 35.0