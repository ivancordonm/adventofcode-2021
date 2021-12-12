def readConnetions(filename):
    c = []
    with open(filename, 'r') as f:
        for line in f:
            con = tuple(line.strip().split('-'))
            if con[0] == 'start':
                c.append(tuple([con[0].capitalize(), con[1]]))
            elif con[1] == 'end':
                c.append(tuple([con[0], con[1].capitalize()]))
            elif con[1] == 'start':
                c.append(tuple([con[1].capitalize(), con[0]]))
            elif con[0] == 'end':
                c.append(tuple([con[1], con[0].capitalize()]))
            else:
                c.append(con)
                c.append(tuple(con[::-1]))
    return c


def recursive_paths(cons, exclude, path):
    c = path[-1][1]
    if c == 'End':
        paths.append(path)
        return
    for elem in cons:
        if elem[0] == 'Start':
            continue
        if (elem[0] == c and elem[0] not in exclude and elem[1] not in exclude) or (elem[0] == c and elem[1] == 'End'):
            if elem[0][0].islower():
                recursive_paths(cons, exclude + [elem[0]], path + [elem])
            else:
                recursive_paths(cons, exclude, path + [elem])


def find_paths(conections):
    for c in conections:
        if c[0] == 'Start':
            conections_copy = conections.copy()
            recursive_paths(conections_copy, [], [c])


if __name__ == '__main__':
    conections = readConnetions("input.txt")
    paths = []
    find_paths(conections)
    # for p in paths:
    #     print(p)

    print("Part 1: ", len(paths))
