def read_balls(fname):
    with open(fname) as f:
        return [int(x) for x in f.readline().split(',')]


def read_boards(fname):
    boards = []
    with open(fname) as f:
        f.readline()
        for line in f:
            if line.strip() == '':
                continue
            board = []
            for i in range(5):
                row = [int(x) for x in line.split()]
                board.append(row)
                line = f.readline()
            iboard = [list(x) for x in zip(*board)]
            boards.append([board, iboard])
    return boards


def flatten(t):
    return [item for sublist in t for item in sublist]


def check_ball(vector, b):
    for row in vector:
        try:
            i = row.index(b)
        except ValueError:
            continue
        row[i] = -1
        b_balls.append(b)
        if sum(row) == -5:
            return sum(flatten(vector)) + flatten(vector).count(-1)
        else:
            return 0
    return 0


def get_winner(boards, balls):
    for b in balls:
        for board in boards:
            result = check_ball(board[0], b)
            if result > 0:
                print(str(result) + "*" + str(b))
                return result * b
            result = check_ball(board[1], b)
            if result > 0:
                print(str(result) + "*" + str(b))
                return result * b


def mark_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            for k in range(len(board[0][0])):
                board[i][j][k] = -1


def get_last_winner(boards, balls):
    for b in balls:
        for board in boards:
            result = check_ball(board[0], b)
            if result > 0:
                # print(str(result) + "*" + str(b))
                print(result * b)
                mark_board(board)
                continue
            result = check_ball(board[1], b)
            if result > 0:
                # print(str(result) + "*" + str(b))
                print(result * b)
                mark_board(board)

            # continue


if __name__ == "__main__":
    b_balls = []
    filename = "input.txt"
    all_balls = read_balls(filename)
    print(all_balls)
    all_boards = read_boards(filename)
    sol = get_winner(all_boards, all_balls)
    print("first winner: " + str(sol))
    get_last_winner(all_boards, all_balls)
