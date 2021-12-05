def to_list(filename):
    with open(filename) as f:
        for line in f:
            instructions_list.append([line.split()[0], int(line.split()[1])])
            # instructions_list.append([x for x in line.split()])


def calculate_distance_1():
    depth = 0
    length = 0
    for [m, v] in instructions_list:
        if m == 'up':
            depth -= v
        elif m == 'down':
            depth += v
        else:
            length += v
    return depth * length


def calculate_distance_2():
    depth = 0
    length = 0
    aim = 0
    for [m, v] in instructions_list:
        if m == 'up':
            aim -= v
        elif m == 'down':
            aim += v
        else:
            length += v
            depth += v * aim
    return depth * length


if __name__ == "__main__":
    instructions_list = []
    to_list("input.txt")

    print("result 1: " + str(calculate_distance_1()))
    print("result 2: " + str(calculate_distance_2()))
