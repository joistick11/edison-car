from PIL import Image

last_direction = []


def get_next_action():
    step_length = 0
    global last_direction
    if image.getpixel((curr_pos[0], curr_pos[1] - 1)) == (0, 0, 0) and last_direction != 'd':
        while image.getpixel((curr_pos[0], curr_pos[1] - 1)) == (0, 0, 0):
            curr_pos[1] -= 1
            step_length += 1
        last_direction = 'u'
        return 'u', step_length
    elif image.getpixel((curr_pos[0], curr_pos[1] + 1)) == (0, 0, 0) and last_direction != 'u':
        while image.getpixel((curr_pos[0], curr_pos[1] + 1)) == (0, 0, 0):
            curr_pos[1] += 1
            step_length += 1
        last_direction = 'd'
        return 'd', step_length
    elif image.getpixel((curr_pos[0] - 1, curr_pos[1])) == (0, 0, 0) and last_direction != 'r':
        while image.getpixel((curr_pos[0] - 1, curr_pos[1])) == (0, 0, 0):
            curr_pos[0] -= 1
            step_length += 1
        last_direction = 'l'
        return 'l', step_length
    elif image.getpixel((curr_pos[0] + 1, curr_pos[1])) == (0, 0, 0) and last_direction != 'l':
        while image.getpixel((curr_pos[0] + 1, curr_pos[1])) == (0, 0, 0):
            curr_pos[0] += 1
            step_length += 1
        last_direction = 'r'
        return 'r', step_length


# image = misc.imread(os.path.join('map_diff.bmp'), flatten=0)
image = Image.open("map.bmp").convert('RGB')

curr_pos = []
for i in range(0, 32):
    for j in range(0, 32):
        if image.getpixel((i, j)) == (255, 0, 0):
            curr_pos = [i, j]
            break

# print(curr_pos)
# last_direction, _ = get_next_action()
# print(last_direction, _)
# print(curr_pos)
# last_direction, _ = get_next_action()
# print(last_direction, _)
# print(curr_pos)
# last_direction, _ = get_next_action()
# print(last_direction, _)
# print(curr_pos)
