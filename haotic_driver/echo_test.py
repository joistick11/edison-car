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


def pulse_in(tick_count):
    pulse_on = dt.now()
    pulse_off = dt.now()
    tick = tick_count
    while echo.read() != 1 and tick != 0:
        pulse_on = dt.now()
        tick -= 1
    tick = tick_count
    while echo.read() != 0 and tick != 0:
        pulse_off = dt.now()
        tick -= 1
    return (pulse_off - pulse_on).microseconds


def send_pulse():
    trig.write(1)
    time.sleep(0.00002)
    trig.write(0)
    return (17 * pulse_in(200) * 0.001)


def calculate_distance(pulse_count):
    distances = np.array([])
    while pulse_count != 0:
        distances = np.append(distances, send_pulse())
        pulse_count = pulse_count - 1;
    return np.mean(reject_outliers(distances))


def has_obstacle():
    return calculate_distance(10) > 35.0


if __name__ == '__main__':
    while True:
        print calculate_distance(10)
        #time.sleep(.2)