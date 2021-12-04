from aocd import get_data
import re
import numpy as np

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)

test_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

class Board:
    def __init__(self, vals):
        self.board = np.array(vals)
        self.guessed = np.full(self.board.shape, False)

    def guess(self, number):
        in_board = np.argwhere(self.board == number)
        if in_board.shape[0] == 1:
            #in the board
            row = in_board[0][0]
            col = in_board[0][1]
            self.guessed[row][col] = 1

    def check_board(self):
        solved = False
        for i in range(self.guessed.shape[0]):
            if all(self.guessed[i, :]) or all(self.guessed[:, i]):
                solved = True

        return solved

def parse_boards(board_data):
    all_boards = []
    for board_raw in board_data:
        board_list = []
        for row in board_raw.split('\n'):
            row_out = []
            for j in row.split(' '):
                if j != ' ' and j != '':
                    row_out.append(int(j))
            board_list.append(row_out)
        b = Board(board_list)
        all_boards.append(b)
    return all_boards

def parse_input(input_data):
    ds = input_data.split('\n\n')
    move_data = ds[0]
    moves = [int(i) for i in move_data.split(',')]
    board_data = ds[1:]
    boards = parse_boards(board_data)
    return moves, boards

def calculate_board_score(board, last_move):
    masked_array = np.ma.array(board.board, mask=board.guessed)
    unguessed_vals = np.sum(masked_array)
    answer = unguessed_vals * last_move
    return answer

def part_one(input_data):
    moves, boards = parse_input(input_data)
    for m in moves:
        for b in boards:
            b.guess(m)
            solved = b.check_board()
            if solved:
                answer = calculate_board_score(b, m)
                print(answer)
                return

def part_two(input_data):
    moves, boards = parse_input(input_data)
    remove = []
    for m in moves:
        for b in boards:
            b.guess(m)
            solved = b.check_board()
            if solved:
                remove.append(b)
        boards = [b for b in boards if b not in remove]
        if len(boards) == 0:
            last_board = remove[-1]
            answer = calculate_board_score(last_board, m)
            print(answer)
            return

part_one(input_data)
part_two(input_data)