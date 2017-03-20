import main_map as bmp_parse
import motors_controller as control
import time


def move(car_path):
    for action in car_path:
        if action[0] == 'u':
            control.run_forward(action[1])
            time.sleep(action[1] / 12.0)
        elif action[0] == 'd':
            control.run_forward(action[1])
            time.sleep(action[1] / 12.0)
        elif action[0] == 'l':
            control.turn_left()
            control.run_forward(action[1])
            time.sleep(action[1] / 12.0)
        elif action[0] == 'r':
            control.turn_right()
            control.run_forward(action[1])
            time.sleep(action[1] / 12.0)
    control.full_stop()

if __name__ == '__main__':
    map_file = "img/map_diff.bmp"
    PATH = bmp_parse.parse_map(map_file)

    try:
        move(PATH)
    except KeyboardInterrupt:
        control.full_stop()
        exit()
