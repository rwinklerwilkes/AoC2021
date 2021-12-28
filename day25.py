from aocd import get_data
import re

# mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
# day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=25)

test_prelim = """...>...
.......
......>
v.....>
......>
.......
..vvv.."""

test_data = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""

def parse_data(input_data):
    rows = input_data.split('\n')
    occupied = {}

    for row_num, row in enumerate(rows):
        for col_num, col in enumerate(row):
            if col == '>':
                occupied[(row_num, col_num)] = 'right'
            elif col == 'v':
                occupied[(row_num, col_num)] = 'down'

    max_row = row_num + 1
    max_col = col_num + 1
    return occupied, max_row, max_col

class Board:
    def __init__(self, input_data):
        occupied, max_row, max_col = parse_data(input_data)
        self.occupied = occupied
        self.max_row = max_row
        self.max_col = max_col

    def __repr__(self):
        new_board = [['_' for col in range(self.max_col)] for row in range(self.max_row)]
        for point, dir in self.occupied.items():
            row_num, col_num = point
            if dir == 'right':
                new_board[row_num][col_num] = '>'
            elif dir == 'down':
                new_board[row_num][col_num] = 'v'
        str_board = [''.join(row) for row in new_board]
        return '\n'.join(str_board)

    def check_adjacent(self, point, direction):
        row_num, col_num = point
        if direction == 'right':
            check = (row_num, (col_num+1)%self.max_col)
        elif direction == 'down':
            check = ((row_num+1)%self.max_row, col_num)

        assert (row_num, col_num) in self.occupied

        if check in self.occupied:
            return check, False
        else:
            return check, True

    def process_move(self, move_direction, stay_direction):
        any_moved = False
        move = [k for k, v in self.occupied.items() if v == move_direction]
        new_occupied = {k:v for k, v in self.occupied.items() if v == stay_direction}
        for point in move:
            new_point, can_move = self.check_adjacent(point, move_direction)
            if can_move:
                any_moved = True
                new_occupied[new_point] = move_direction
            else:
                new_occupied[point] = move_direction
        self.occupied = new_occupied
        return any_moved

    def run_round(self):
        any_moved_right = self.process_move('right', 'down')
        any_moved_down = self.process_move('down', 'right')
        return any([any_moved_right, any_moved_down])


def part_one(input_data):
    b = Board(input_data)
    round_counter = 0
    while True:
        any_moved = b.run_round()
        round_counter += 1
        if not any_moved:
            break

    answer = round_counter
    print(answer)

part_one(input_data)