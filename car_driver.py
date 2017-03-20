import main_map as bmp_parse
import motors_controller as control
import time


def move(car_path):
    for action in car_path:
        action_time = action[1] / 10.0
        print(str(action[0]) + " " + str(action_time))
        if action[0] == 'f':
            control.run_forward(action_time)
        elif action[0] == 'l':
            control.turn_left()
            control.run_forward(action_time)
        elif action[0] == 'r':
            control.turn_right()
            control.run_forward(action_time)
        elif action[0] == 'b':
            control.turn_right()
            control.turn_right()
    control.full_stop()

if __name__ == '__main__':
    map_file = "img/perekrestok.bmp"
    PATH = bmp_parse.parse_map(map_file)

    try:
        move(PATH)
    except KeyboardInterrupt:
        control.full_stop()
        exit()
