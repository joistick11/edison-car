import operator
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
        step_length = 0
        if image.getpixel((current_pos[0], current_pos[1] - 1)) in ((0, 0, 0), (0, 255, 0)) and last_direction != 'd':
            while image.getpixel((current_pos[0], current_pos[1] - 1)) in ((0, 0, 0), (0, 255, 0)):
                current_pos[1] -= 1
                step_length += 1
            last_direction = 'u'
            action_chain.append(('u', step_length))
        elif image.getpixel((current_pos[0], current_pos[1] + 1)) in ((0, 0, 0), (0, 255, 0)) and last_direction != 'u':
            while image.getpixel((current_pos[0], current_pos[1] + 1)) in ((0, 0, 0), (0, 255, 0)):
                current_pos[1] += 1
                step_length += 1
            last_direction = 'd'
            action_chain.append(('d', step_length))
        elif image.getpixel((current_pos[0] - 1, current_pos[1])) in ((0, 0, 0), (0, 255, 0)) and last_direction != 'r':
            while image.getpixel((current_pos[0] - 1, current_pos[1])) in ((0, 0, 0), (0, 255, 0)):
                current_pos[0] -= 1
                step_length += 1
            last_direction = 'l'
            action_chain.append(('l', step_length))
        elif image.getpixel((current_pos[0] + 1, current_pos[1])) in ((0, 0, 0), (0, 255, 0)) and last_direction != 'l':
            while image.getpixel((current_pos[0] + 1, current_pos[1])) in ((0, 0, 0), (0, 255, 0)):
                current_pos[0] += 1
                step_length += 1
            last_direction = 'r'
            action_chain.append(('r', step_length))
    return action_chain


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
    elif current_abs == 'r':
        if candidate_abs == 'u':
            return 'left'
        elif candidate_abs == 'd':
            return 'right'
    elif current_abs == 'd':
        if candidate_abs == 'r':
            return 'left'
        elif candidate_abs == 'l':
            return 'right'
    elif current_abs == 'l':
        if candidate_abs == 'u':
            return 'right'
        elif candidate_abs == 'd':
            return 'left'


def parse_map(map_file):
    image = Image.open(map_file).convert('RGB')
    return convert_absolute_to_relative_action_chain(get_absolute_action_chain(find_start_point(image), image))

