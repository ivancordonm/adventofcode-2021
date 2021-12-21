import re
import sys


def read_input(filename):
    with open(filename) as f:
        line = f.readline()

    pattern_x = '.+x=(-?[0-9]+)..(-?[0-9]+)'
    pattern_y = '.+y=(-?[0-9]+)..(-?[0-9]+)'

    result_x = re.match(pattern_x, line)
    result_y = re.match(pattern_y, line)

    return (int(result_x.group(1)), int(result_x.group(2))), (int(result_y.group(1)), int(result_y.group(2)))


def in_target(x, y):
    return target[0][0] <= x <= target[0][1] and target[1][0] <= y <= target[1][1]


def out_of_target(x, y):
    return x > target[0][1] or y < target[1][0]


def launch_probe():
    res = (0, 0)
    highest_y = -sys.maxsize
    for i in range(200):
        for j in range(200):
            x, y = 0, 0
            i_ = i
            j_ = j
            local_highest = 0
            while not out_of_target(x, y):
                if in_target(x, y):
                    if local_highest > highest_y:
                        highest_y = local_highest
                        res = highest_y
                x += i_
                y += j_
                if y > local_highest:
                    local_highest = y
                if i_ > 0:
                    i_ -= 1
                j_ -= 1
    return res


if __name__ == '__main__':
    target = read_input('input.txt')
    print(launch_probe())
