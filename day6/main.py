def read_input(filename):
    with open(filename) as f:
        return [int(x) for x in f.readline().split(',')]


def add_new_fishes(new_fishes):
    for i in range(new_fishes):
        fishes.append(8)


def grow_fishes(days):
    for i in range(days):
        new_fishes = 0
        for idx, fish in enumerate(fishes):
            if fish > 0:
                fishes[idx] -= 1
            elif fish == 0:
                fishes[idx] = 6
                new_fishes += 1
        add_new_fishes(new_fishes)
        # if i % 10 == 0:
        #     print(i)


def calculate_groups():
    grouped_fishes = [0] * 9
    for fish in fishes:
        grouped_fishes[fish] += 1
    return grouped_fishes


def grow_fishes_optimized(days):
    gfishes = calculate_groups()

    for i in range(days):
        g0 = gfishes[0]
        gfishes[0] = 0
        for idx in range(1, len(gfishes)):
            gfishes[idx - 1] += gfishes[idx]
            gfishes[idx] = 0
        gfishes[6] += g0
        gfishes[8] = g0

        # if i % 10 == 0:
        #     print(i)
    return gfishes


if __name__ == "__main__":
    # fishes = read_input("test.txt")
    fishes = read_input("input.txt")
    grow_fishes(80)
    print(len(fishes))
    _gfishes = grow_fishes_optimized(256)
    print(sum(_gfishes))
