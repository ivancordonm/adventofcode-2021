def read_board(filename):
    with open(filename, 'r') as f:
        for line in f:
            board.append([int(x) for v in line.split() for x in v])


def calculate_mins():
    low_points = []
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if i > 0 and board[i - 1][j] < board[i][j]:
                continue
            if j > 0 and board[i][j - 1] < board[i][j]:
                continue
            if i < len(board) - 1 and board[i + 1][j] < board[i][j]:
                continue
            if j < len(board[i]) - 1 and board[i][j + 1] < board[i][j]:
                continue
            low_points.append(board[i][j] + 1)
    return sum(low_points)


if __name__ == '__main__':
    board = []
    read_board("input.txt")
    # read_board("test.txt")
    total = calculate_mins()
    print("Part 1:", total)
