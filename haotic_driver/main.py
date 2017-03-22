import random

from echo_sensor import has_obstacle
from motors_controller import run_forward, full_stop, turn_right, turn_left
import pyupm_buzzer as upmBuzzer

buzzer = upmBuzzer.Buzzer(9)


def make_bip():
    buzzer.playSound(upmBuzzer.MI, 100000)  # delay in microseconds


def make_decision():
    if random.randint(0, 1):
        turn_right()
    else:
        turn_left()


if __name__ == '__main__':
    try:
        while True:
            if not has_obstacle():
                run_forward(1)
            else:
                full_stop()
                make_decision()
    except KeyboardInterrupt:
        full_stop()
        exit(1)


