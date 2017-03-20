import mraa
import time
from datetime import datetime as dt

TRIG_PIN = 10
ECHO_PIN = 11

trig = mraa.Gpio(TRIG_PIN)
echo = mraa.Gpio(ECHO_PIN)

trig.dir(mraa.DIR_OUT)
echo.dir(mraa.DIR_IN)


def pulseIn():
    pulseOn = 0
    pulseOff = 0
    while echo.read() == 0:
        pulseOn = dt.now()
    while echo.read() == 1:
        pulseOff = dt.now()
    return pulseOff - pulseOn

if __name__ == "__main__":
    try:
        while True:
            trig.write(1)
            time.sleep(1)
            trig.write(0)
            print (17000 * pulseIn().microseconds * 0.000001)
    except KeyboardInterrupt:
        exit()

