from functools import reduce


def read_board(filename):
    with open(filename, 'r') as f:
        for line in f:
            board.append([int(x) for v in line.split() for x in v])


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


def recursive_basins(board):
    lp = calculate_mins()
    calculate_basins(lp)

def calculate_basins(lp):
    for p in lp:



if __name__ == '__main__':
    board = []
    # read_board("input.txt")
    read_board("test.txt")
    low_points = calculate_mins()
    print("Part 1:", reduce(lambda x, y: x + y, [board[x][y] + 1 for x, y in low_points]))
    basins = calculate_basins(low_points)
    print("Part 2:", sum(basins))