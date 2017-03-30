import random

from echo_sensor import has_obstacle
from motors_controller import *
import pyupm_buzzer as upmBuzzer

buzzer = upmBuzzer.Buzzer(9)
buzzer.stopSound()


def make_bip():
    print("beep")
    buzzer.playSound(upmBuzzer.MI, 100000)  # delay in microseconds


def make_decision():
    print("decision")
    if random.randint(0, 1):
        print("right")
        turn_right()
    else:
        print("left")
        turn_left()


if __name__ == '__main__':
    try:
        while True:
	    #time.sleep(.2)
            if not has_obstacle():
                run_forward(.1)
                print("forward")
            else:
                make_bip()
                print("obstacle")
                full_stop()
                #run_backward(1)
                make_decision()
    except KeyboardInterrupt:
        full_stop()
        exit(1)


