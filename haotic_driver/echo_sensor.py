import mraa
import time
from datetime import datetime as dt

TRIG_PIN = 10
ECHO_PIN = 11

trig = mraa.Gpio(TRIG_PIN)
echo = mraa.Gpio(ECHO_PIN)

trig.dir(mraa.DIR_OUT)
echo.dir(mraa.DIR_IN)


def pulse_in():
    try:
        pulse_on = 0
        pulse_off = 0
        while echo.read() == 0:
            pulse_on = dt.now()
        while echo.read() == 1:
            pulse_off = dt.now()
        return pulse_off - pulse_on
    except:
        return 42


def has_obstacle():
    trig.write(1)
    time.sleep(1)
    trig.write(0)
    return (17000 * pulse_in().microseconds * 0.000001) < 20.0