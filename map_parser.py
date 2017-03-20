import operator
import random as rand

from PIL import Image


def find_start_point(image):
    for i in range(0, 32):
        for j in range(0, 32):
            if image.getpixel((i, j)) == (255, 0, 0):
                return i, j


def get_absolute_action_chain(start_pos, image):
    current_pos = list(start_pos)
    action_chain = []
    last_direction = None
    while image.getpixel(tuple(current_pos)) != (0, 255, 0):
        available_directions = []
        if image.getpixel((current_pos[0], current_pos[1] - 1)) in ((0, 0, 0), (0, 255, 0)) and last_direction != 'd':
            available_directions.append('u')
        if image.getpixel((current_pos[0], current_pos[1] + 1)) in ((0, 0, 0), (0, 255, 0)) and last_direction != 'u':
            available_directions.append('d')
        if image.getpixel((current_pos[0] - 1, current_pos[1])) in ((0, 0, 0), (0, 255, 0)) and last_direction != 'r':
            available_directions.append('l')
        if image.getpixel((current_pos[0] + 1, current_pos[1])) in ((0, 0, 0), (0, 255, 0)) and last_direction != 'l':
            available_directions.append('r')

        # dead end
        if len(available_directions) == 0:
            if last_direction == 'u':
                backward = 'd'
            elif last_direction == 'd':
                backward = 'u'
            elif last_direction == 'r':
                backward = 'l'
            elif last_direction == 'l':
                backward = 'r'
            step_length = move_to_next_cross(backward, image, current_pos)
            action_chain.append((backward, step_length))
            continue

        rand_direction_index = rand.randint(0, len(available_directions) - 1)
        last_direction = available_directions[rand_direction_index]
        step_length = move_to_next_cross(last_direction, image, current_pos)
        action_chain.append((last_direction, step_length))
        print(action_chain)
    return action_chain


def move_to_next_cross(direction, image, current_pos):
    step_length = 0
    if direction == 'u':
        current_pos[1] -= 1
        step_length += 1
        while image.getpixel((current_pos[0], current_pos[1] - 1)) in ((0, 0, 0), (0, 255, 0)) \
                and image.getpixel((current_pos[0] - 1, current_pos[1])) not in ((0, 0, 0), (0, 255, 0)) \
                and image.getpixel((current_pos[0] + 1, current_pos[1])) not in ((0, 0, 0), (0, 255, 0)):
            current_pos[1] -= 1
            step_length += 1
    elif direction == 'd':
        current_pos[1] += 1
        step_length += 1
        while image.getpixel((current_pos[0], current_pos[1] + 1)) in ((0, 0, 0), (0, 255, 0)) \
                and image.getpixel((current_pos[0] - 1, current_pos[1])) not in ((0, 0, 0), (0, 255, 0)) \
                and image.getpixel((current_pos[0] + 1, current_pos[1])) not in ((0, 0, 0), (0, 255, 0)):
            current_pos[1] += 1
            step_length += 1
    elif direction == 'l':
        current_pos[0] -= 1
        step_length += 1
        while image.getpixel((current_pos[0] - 1, current_pos[1])) in ((0, 0, 0), (0, 255, 0)) \
                and image.getpixel((current_pos[0], current_pos[1] - 1)) not in ((0, 0, 0), (0, 255, 0)) \
                and image.getpixel((current_pos[0], current_pos[1] + 1)) not in ((0, 0, 0), (0, 255, 0)):
            current_pos[0] -= 1
            step_length += 1
    elif direction == 'r':
        current_pos[0] += 1
        step_length += 1
        while image.getpixel((current_pos[0] + 1, current_pos[1])) in ((0, 0, 0), (0, 255, 0)) \
                and image.getpixel((current_pos[0], current_pos[1] - 1)) not in ((0, 0, 0), (0, 255, 0)) \
                and image.getpixel((current_pos[0], current_pos[1] + 1)) not in ((0, 0, 0), (0, 255, 0)):
            current_pos[0] += 1
            step_length += 1
    return step_length


def convert_absolute_to_relative_action_chain(absolute_action_chain):
    # calculate relative directions
    directions = list(map(operator.itemgetter(0), absolute_action_chain))
    current_abs = directions.pop(0)
    relative_action_chain = ['forward']
    while len(directions) > 0:
        candidate_abs = directions.pop(0)
        relative_action_chain.append(calculate_relative_with_new_abs(current_abs, candidate_abs))
        current_abs = candidate_abs

    # append relative directions with length
    return list(map(lambda item: (item[1][0], item[0][1]), zip(absolute_action_chain, relative_action_chain)))


def calculate_relative_with_new_abs(current_abs, candidate_abs):
    if current_abs == 'u':
        if candidate_abs == 'l':
            return 'left'
        elif candidate_abs == 'r':
            return 'right'
        elif candidate_abs == 'd':
            return 'backward'
    elif current_abs == 'r':
        if candidate_abs == 'u':
            return 'left'
        elif candidate_abs == 'd':
            return 'right'
        elif candidate_abs == 'l':
            return 'backward'
    elif current_abs == 'd':
        if candidate_abs == 'r':
            return 'left'
        elif candidate_abs == 'l':
            return 'right'
        elif candidate_abs == 'u':
            return 'backward'
    elif current_abs == 'l':
        if candidate_abs == 'u':
            return 'right'
        elif candidate_abs == 'd':
            return 'left'
        elif candidate_abs == 'r':
            return 'backward'
    return 'f'


def parse_map(map_file):
    image = Image.open(map_file).convert('RGB')
    return convert_absolute_to_relative_action_chain(get_absolute_action_chain(find_start_point(image), image))


if __name__ == '__main__':
    print(parse_map("img/perekrestok.bmp"))
