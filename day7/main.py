import statistics
import sys


def calculate_fuel1():
    total = 0
    m = median(positions)
    for elem in positions:
        total += abs(elem - m)
    return total


def calculate_fuel2():
    min_fuel = sys.maxsize
    min_m = 0
    for m in range(min(positions), max(positions) + 1):
        partial_total = 0
        for elem in positions:
            d = abs(elem - m)
            partial_total += d * (d + 1) / 2
        if partial_total < min_fuel:
            min_fuel = partial_total
            min_m = m
    return min_fuel


def median(lst):
    return statistics.median(lst)


def read_positions(filename):
    with open(filename) as f:
        return [int(x) for x in f.readline().split(',')]


if __name__ == "__main__":
    positions = read_positions("input.txt")
    # positions = read_positions("test.txt")
    print(f"Total fuel1: {calculate_fuel1()}")
    print(f"Total fuel2: {calculate_fuel2()}")
