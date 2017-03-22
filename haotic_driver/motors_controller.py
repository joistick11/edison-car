import mraa
import time

PIN_LEFT_P = 4
PIN_LEFT_M = 5
PIN_RIGHT_P = 6
PIN_RIGHT_M = 7

wh1p = mraa.Gpio(PIN_LEFT_P)
wh1m = mraa.Gpio(PIN_LEFT_M)
wh2p = mraa.Gpio(PIN_RIGHT_P)
wh2m = mraa.Gpio(PIN_RIGHT_M)

wh1p.dir(mraa.DIR_OUT)
wh1m.dir(mraa.DIR_OUT)
wh2p.dir(mraa.DIR_OUT)
wh2m.dir(mraa.DIR_OUT)


def left_forward():
    wh1p.write(1)
    wh1m.write(0)


def left_backward():
    wh1p.write(0)
    wh1m.write(1)


def right_forward():
    wh2p.write(0)
    wh2m.write(1)


def right_backward():
    wh2p.write(1)
    wh2m.write(0)


def run_forward(seconds):
    right_forward()
    left_forward()
    time.sleep(seconds)


def run_backward(seconds):
    right_backward()
    left_backward()
    time.sleep(seconds)


def full_stop():
    wh1p.write(0)
    wh1m.write(0)
    wh2p.write(0)
    wh2m.write(0)


def right_wheel_stop():
    wh2p.write(0)
    wh2m.write(0)


def left_wheel_stop():
    wh1p.write(0)
    wh1m.write(0)


def turn_right():
    left_forward()
    right_backward()
    time.sleep(0.6)


def turn_left():
    right_forward()
    left_backward()
    time.sleep(0.6)
