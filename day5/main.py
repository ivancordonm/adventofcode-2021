def read_line(filename):
    with open(filename) as f:
        for line in f:
            [start, end] = line.split('->')
            start_vector = [int(x) for x in start.split(',')]
            end_vector = [int(x) for x in end.split(',')]
            lines.append([start_vector, end_vector])


def max_value(matrix):
    return max(map(max, flatten(matrix)))


def flatten(t):
    return [item for sublist in t for item in sublist]


def is_vertical_or_horizontal(vector):
    [p0, p1] = vector
    if p0[0] == p1[0] or p0[1] == p1[1]:
        return True
    else:
        return False


def vector_sign(vector):
    [p0, p1] = vector
    if p1[0] - p0[0] >= 0:
        s0 = 1
    else:
        s0 = -1

    if p1[1] - p0[1] >= 0:
        s1 = 1
    else:
        s1 = -1

    return [s0, s1]


def is_diagonal(vector):
    [p0, p1] = vector
    s = (p1[0] - p0[0]) / (p1[1] - p0[1])
    if s == 1 or s == -1:
        return True
    else:
        return False


def sort_points(vector):
    if vector[0][0] == vector[1][0]:
        return sorted(vector, key=lambda x: x[1], reverse=False)
    else:
        return sorted(vector, key=lambda x: x[0], reverse=False)


def mark_in_board_vh(board):
    for vector in lines:
        if is_vertical_or_horizontal(vector):
            [p0, p1] = sort_points(vector)
            for i in range(p0[0], p1[0] + 1):
                for j in range(p0[1], p1[1] + 1):
                    board[i][j] += 1


def mark_in_board_vhd(board):
    for vector in lines:
        if is_vertical_or_horizontal(vector):
            [p0, p1] = sort_points(vector)
            for i in range(p0[0], p1[0] + 1):
                for j in range(p0[1], p1[1] + 1):
                    board[i][j] += 1
        elif is_diagonal(vector):
            s = vector_sign(vector)
            [p0, p1] = vector
            for i, j in zip(range(p0[0], p1[0] + s[0], s[0]), range(p0[1], p1[1] + s[1], s[1])):
                board[i][j] += 1


def count_overlapping_points(board):
    count = 0
    for i in range(upper):
        for j in range(upper):
            if board[i][j] > 1:
                count += 1
    print(count)


if __name__ == "__main__":
    lines = []
    # read_line("test.txt")
    read_line("input.txt")
    upper = max_value(lines) + 1
    # board1 = [[0 for x in range(upper)] for y in range(upper)]
    # mark_in_board_vh(board1)
    # count_overlapping_points(board1)
    board2 = [[0 for x in range(upper)] for y in range(upper)]
    mark_in_board_vhd(board2)
    count_overlapping_points(board2)
