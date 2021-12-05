def to_list(filename):
    with open(filename) as f:
        for line in f:
            data.append(list(line.rstrip()))


def invert_element(element):
    if element == '0':
        return '1'
    else:
        return '0'


def max_element(row, elem):
    ones = row.count('1')
    zeros = len(row) - ones
    if ones > zeros:
        return '1'
    elif zeros > ones:
        return '0'
    else:
        return elem


def min_element(row, elem):
    ones = row.count('1')
    zeros = len(row) - ones
    if ones > zeros:
        return '0'
    elif zeros > ones:
        return '1'
    else:
        return elem


def calculate_1(r_list):
    # transpose = list(zip(*data))
    gamma_r = []
    epsilon_r = []
    for i in range(len(r_list)):
        elem = max_element(r_list[i], '1')
        gamma_r.append(elem)
        elem = min_element(r_list[i], '0')
        epsilon_r.append(elem)
    gamma = int(''.join(gamma_r), 2)
    epsilon = int(''.join(epsilon_r), 2)
    print(epsilon * gamma)


def reduce(left, elem, size):
    for i in range(size):
        left_b = left
        if len(left_b) > 1:
            if elem == '1':
                c = max_element(list(zip(*left_b))[i], elem)
            else:
                c = min_element(list(zip(*left_b))[i], elem)

            left_b = list(filter(lambda d: d[i] == c, left_b))
            if len(left_b) == 0:
                continue
            else:
                left = left_b
        else:
            break
    return left


def calculate_2(r_list):
    oxigen_l = scrubber_l = data
    oxigen_l = reduce(oxigen_l, '1', len(r_list))
    scrubber_l = reduce(scrubber_l, '0', len(r_list))

    oxigen = int(''.join(oxigen_l[0]), 2)
    scrubber = int(''.join(scrubber_l[0]), 2)

    print(oxigen)
    print(scrubber)

    print(oxigen * scrubber)


if __name__ == "__main__":
    data = []
    to_list("input.txt")
    transpose = list(zip(*data))
    calculate_1(transpose)
    calculate_2(transpose)
