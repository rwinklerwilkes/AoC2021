from aocd import get_data
import re
import numpy as np

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)

test_data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

def parse_input(input_data):
    parsed_data = []
    max_x = 0
    max_y = 0
    for points_raw in input_data.split('\n'):
        pts = points_raw.split(' -> ')
        pts_out = []
        for pt in pts:
            pts = pt.split(',')
            x = int(pts[0])
            if x > max_x:
                max_x = x
            y = int(pts[1])
            if y > max_y:
                max_y = y
            pts_out.append((x, y))
        parsed_data.append(pts_out)

    empty_array = np.zeros((max_x+1, max_y+1))
    return parsed_data, empty_array

def part_one(input_data):
    input_data, empty_array = parse_input(input_data)

    for both_points in input_data:
        start_col, start_row = both_points[0]
        end_col, end_row = both_points[1]
        #Need to swap positions if one is closer to the top left
        if (end_row + end_col) < (start_row + start_col):
            temp_end_row, temp_end_col = end_row, end_col
            end_row, end_col = start_row, start_col
            start_row, start_col = temp_end_row, temp_end_col

        if start_col == end_col or start_row == end_row:
            if start_col != end_col:
                for i in range(start_col, end_col+1):
                    empty_array[start_row, i] += 1
            elif start_row != end_row:
                for i in range(start_row, end_row+1):
                    empty_array[i, start_col] += 1

    answer = np.where(empty_array >= 2)[0].shape[0]
    print(answer)

def get_diagonals(start, end):
    start_row, start_col = start
    end_row, end_col = end
    d_row = np.sign(end_row-start_row)
    d_col = np.sign(end_col-start_col)
    diagonals = []
    row, col = start_row, start_col
    while row != end_row+d_row and col != end_col+d_col:
        diagonals.append((row, col))
        row += d_row
        col += d_col
    return diagonals


def part_two(input_data):
    input_data, empty_array = parse_input(input_data)

    for both_points in input_data:
        start_col, start_row = both_points[0]
        end_col, end_row = both_points[1]
        #Need to swap positions if one is closer to the top left
        check_pos = (end_row + end_col) - (start_row + start_col)
        if check_pos < 0:
            temp_end_row, temp_end_col = end_row, end_col
            end_row, end_col = start_row, start_col
            start_row, start_col = temp_end_row, temp_end_col

        if start_col == end_col or start_row == end_row:
            if start_col != end_col:
                for i in range(start_col, end_col+1):
                    empty_array[start_row, i] += 1
            elif start_row != end_row:
                for i in range(start_row, end_row+1):
                    empty_array[i, start_col] += 1
        else:
            diag = get_diagonals((start_row, start_col), (end_row, end_col))
            for i, j in diag:
                empty_array[i][j] += 1

    answer = np.where(empty_array >= 2)[0].shape[0]
    print(answer)

part_one(input_data)
part_two(input_data)