def parse_actions_from_file(path_to_file):
    actions = []
    with open(path_to_file) as path_file:
        for row in path_file:
            direction, step_length = row.split(" ")
            step_length = step_length.replace("\n", '')
            actions.append((direction, int(step_length)))
    return actions


if __name__ == '__main__':
    print(parse_actions_from_file("path/square_and_back_to_start"))
