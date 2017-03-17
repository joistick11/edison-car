import mraa
import time

from main_map import get_next_action

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


def run_forward():
    right_forward()
    left_forward()

def run_backward():
    right_backward()
    left_backward()

def full_stop():
    wh1p.write(0)
    wh1m.write(0)
    wh2p.write(0)
    wh2m.write(0)

def right_stop():
    wh2p.write(0)
    wh2m.write(0)

def left_stop():
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


if __name__ == "__main__":
    try:
        while True:
            action = get_next_action()
            if not action:
                break

            print action

            if action[0] == 'u':
                print action[1] / 7.0
                run_forward()
                time.sleep(action[1] / 12.0)
            elif action[0] == 'd':
                run_forward()
                print action[1] / 7.0
                time.sleep(action[1] / 12.0)
            elif action[0] == 'l':
                turn_left()
                print action[1] / 7.0
                run_forward()
                time.sleep(action[1] / 12.0)
            elif action[0] == 'r':
                turn_right()
                print action[1] / 7.0
                run_forward()
                time.sleep(action[1] / 12.0)

        full_stop()
    except KeyboardInterrupt:
        full_stop()
        print "ok"
        exit()
