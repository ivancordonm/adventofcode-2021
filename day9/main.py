import operator
from functools import reduce


def calculate_mins():
    lp = []
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if i > 0 and board[i - 1][j] <= board[i][j]:
                continue
            if j > 0 and board[i][j - 1] <= board[i][j]:
                continue
            if i < len(board) - 1 and board[i + 1][j] <= board[i][j]:
                continue
            if j < len(board[i]) - 1 and board[i][j + 1] <= board[i][j]:
                continue
            lp.append((i, j))
    return lp


def read_board(filename):
    with open(filename, 'r') as f:
        for line in f:
            board.append([int(x) for v in line.split() for x in v])


def recursive_basins(p, s=0):
    i, j = p
    if i > 0 and board[i][j] < board[i - 1][j] < 9:
        s = recursive_basins((i - 1, j), s)
    if j > 0 and board[i][j] < board[i][j - 1] < 9:
        s = recursive_basins((i, j - 1), s)
    if i < len(board) - 1 and board[i][j] < board[i + 1][j] < 9:
        s = recursive_basins((i + 1, j), s)
    if j < len(board[i]) - 1 and board[i][j] < board[i][j + 1] < 9:
        s = recursive_basins((i, j + 1), s)
    board[i][j] = 9
    return s + 1


def calculate_basins(lp):
    b = []
    for p in lp:
        b.append(recursive_basins(p))
    return b


if __name__ == '__main__':
    board = []
    read_board("input.txt")
    # read_board("test2.txt")
    # read_board("test.txt")

    low_points = calculate_mins()
    print("Part 1:", reduce(lambda x, y: x + y, [board[x][y] + 1 for x, y in low_points]))
    basins = calculate_basins(low_points)
    print("Part 2:", reduce(operator.mul, sorted(basins, reverse=True)[0:3], 1))
