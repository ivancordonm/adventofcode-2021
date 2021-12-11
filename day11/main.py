def read_octopus_board(filename):
    board = []
    with open(filename) as f:
        for line in f:
            board.append([int(x) for x in line.strip()])
    return board


def increase_element(element):
    if element == 9:
        return 0
    else:
        return element + 1


def adjacent_flashes(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i < 0 or i >= len(board) - 1 or j < 0 or j >= len(board[i]) - 1:
                continue
            if 9 == board[i - 1][j - 1] \
                    == board[i][j - 1] \
                    == board[i + 1][j - 1] \
                    == board[i + 1][j] \
                    == board[i + 1][j + 1] \
                    == board[i][j + 1] \
                    == board[i - 1][j + 1] \
                    == board[i - 1][j]:
                octopus_board[i][j] = 9


def recursive_increment(p):
    i, j = p
    adjacent_flashes(octopus_board)
    if octopus_board[i][j] != 0:
        octopus_board[i][j] = increase_element(octopus_board[i][j])
    if octopus_board[i][j] == 0:
        # ⬆️
        if i > 0 and octopus_board[i - 1][j] != 0:
            recursive_increment((i - 1, j))
        # ↖️
        if i > 0 and j > 0 and octopus_board[i - 1][j - 1] != 0:
            recursive_increment((i - 1, j - 1))
        # ⬅️
        if j > 0 and octopus_board[i][j - 1] != 0:
            recursive_increment((i, j - 1))
        # ↙️
        if i < len(octopus_board) - 1 and j > 0 and octopus_board[i + 1][j - 1] != 0:
            recursive_increment((i + 1, j - 1))
        # ⬇️
        if i < len(octopus_board) - 1 and octopus_board[i + 1][j] != 0:
            recursive_increment((i + 1, j))
        # ↘️
        if i < len(octopus_board) - 1 and j < len(octopus_board[i]) - 1 and octopus_board[i + 1][j + 1] != 0:
            recursive_increment((i + 1, j + 1))
        # ➡️
        if j < len(octopus_board[i]) - 1 and octopus_board[i][j + 1] != 0:
            recursive_increment((i, j + 1))
        # ↗️
        if i > 0 and j < len(octopus_board) - 1 > 0 and octopus_board[i - 1][j + 1] != 0:
            recursive_increment((i - 1, j + 1))


def total_flashes(board):
    t = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 0:
                t += 1
    return t


def run_step(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            board[i][j] = increase_element(board[i][j])

    zero_points = []
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 0:
                zero_points.append((i, j))

    for p in zero_points:
        recursive_increment(p)


def count_flashes(board, steps):
    # print(board)
    t = 0
    for _ in range(steps):
        run_step(board)
        t += total_flashes(board)
    return t


def all_flashing(board, count=0):
    t = 0
    while t != len(board) * len(board[0]):
        count += 1
        run_step(board)
        t = total_flashes(board)
    return count


if __name__ == "__main__":
    octopus_board = read_octopus_board("input.txt")
    print(octopus_board)
    total = count_flashes(octopus_board, 100)
    print(octopus_board)
    print(total)
    print(all_flashing(octopus_board, 100))
    print(octopus_board)
