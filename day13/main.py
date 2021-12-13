import re


def read_paper(filename):
    fs = []
    points = []
    with open(filename) as f:
        for line in f:
            if line == '\n':
                break
            points.append(tuple([int(x) for x in line.strip().split(',')]))
        for line in f:
            _, _, variable, value = re.split(r'=|\s', line.strip())
            fs.append((variable, int(value)))
    return points, fs


def fill_paper(d, f, n=1):
    max_x = max(d, key=lambda x: x[0])[0]
    max_y = max(d, key=lambda x: x[1])[1]
    paper = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for dot in d:
        paper[dot[1]][dot[0]] = '#'

    if n == 0:
        n = len(f)
    for idx in range(n):
        fold = f[idx]
        if fold[0] == 'y':
            for i in range(1, max_y - fold[1] + 1):
                for j in range(max_x + 1):
                    if paper[fold[1] + i][j] == '#':
                        paper[fold[1] - i][j] = paper[fold[1] + i][j]
            max_y = fold[1] - 1
            paper[:] = paper[:max_y + 1][:]
        else:
            for j in range(1, max_x - fold[1] + 1):
                for i in range(max_y + 1):
                    if paper[i][fold[1] + j] == '#':
                        paper[i][fold[1] - j] = paper[i][fold[1] + j]
            max_x = fold[1] - 1
            paper[:] = [x[:max_x + 1] for x in paper]
    return paper


def count_dots(r):
    return sum(x.count('#') for x in r)


if __name__ == '__main__':
    dots, folds = read_paper("input.txt")
    result = fill_paper(dots, folds)
    print("Part 1: ", count_dots(result))
    result = fill_paper(dots, folds, 0)
    print("Part 2: ", count_dots(result))
    for d in result:
        print(d)
