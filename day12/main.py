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


def is_excluded(element, exclude, max_exclude):
    if max_exclude == 1:
        return element[0] in exclude or element[1] in exclude
    else:
        if len(exclude) > 0:
            max_elemnt = max(set(exclude), key=exclude.count)
            if exclude.count(max_elemnt) > 1:
                return element[0] in exclude or element[1] in exclude
            else:
                return element[0] in exclude and element[1] in exclude
        return False


def recursive_paths(cons, exclude, path, n):
    c = path[-1][1]
    if c == 'End':
        paths.append(path)
        return
    for elem in cons:
        if elem[0] == 'Start':
            continue
        if (elem[0] == c and not is_excluded(elem, exclude, n)) or (elem[0] == c and elem[1] == 'End'):
            if elem[0][0].islower():
                recursive_paths(cons, exclude + [elem[0]], path + [elem], n)
            else:
                recursive_paths(cons, exclude, path + [elem], n)


def find_paths(conections, n=1):
    for c in conections:
        if c[0] == 'Start':
            conections_copy = conections.copy()
            recursive_paths(conections_copy, [], [c], n)


if __name__ == '__main__':
    conections = readConnetions("input.txt")

    paths = []
    find_paths(conections)
    print("Part 1: ", len(paths))

    paths = []
    find_paths(conections, 2)
    print("Part 2: ", len(paths))
