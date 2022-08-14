def is_column_marked(board):
    win = False
    for i in range(5):
        if any([x[i] != -1 for x in board]):
            continue
        win = True
        break
    return win


def is_row_marked(board):
    win = False
    for i in range(5):
        if any([x != -1 for x in board[i]]):
            continue
        win = True
        break
    return win


def is_board_wins(board):
    return is_row_marked(board) or is_column_marked(board)


def mark(number, board):
    return [[x if x != number else -1 for x in row] for row in board]


def sum_board(board):
    return sum([sum(row) for row in [[x if x != -1 else 0 for x in row] for row in board]])


def main():
    f = open('./input.txt', 'r')
    num_to_draw = list(map(lambda x: int(x), f.readline().strip().split(',')))
    lines = f.readlines()
    lines = list(filter(lambda x: x != '', map(lambda x: x.strip(), lines)))

    boards = []
    i = 0
    board = []
    for line in lines:
        if i == 0:
            board = [list(map(lambda x: int(x.strip()), line.split()))]
            i += 1
        elif i < 4:
            board.append(list(map(lambda x: int(x.strip()), line.split())))
            i += 1
        else:
            board.append(list(map(lambda x: int(x.strip()), line.split())))
            boards.append(board)
            i = 0

    winning_sum = -1
    for num in num_to_draw:
        for i in range(len(boards)):
            boards[i] = mark(num, boards[i])
            if is_board_wins(boards[i]):
                winning_sum = sum_board(boards[i])
                break
        if winning_sum != -1:
            print(num)
            break
    print(winning_sum)


if __name__ == '__main__':
    main()
