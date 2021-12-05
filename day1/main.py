def simple_counter():
    count = 0
    last = measurements[0]
    for item in measurements[1:]:
        if item > last:
            count += 1
        last = item
    return count


def triple_counter():
    count = 0
    last_sum = sum(measurements[0:3])
    for i in range(1, len(measurements)):
        actual_sum = sum(measurements[i:i+3])
        if actual_sum > last_sum:
            count += 1
        last_sum = actual_sum
    return count


def to_list(filename):
    with open(filename) as f:
        for item in f:
            measurements.append(int(item))


if __name__ == '__main__':
    measurements = []
    to_list("input.txt")
    print('part 1: ' + str(simple_counter()))
    print('part 2: ' + str(triple_counter()))
