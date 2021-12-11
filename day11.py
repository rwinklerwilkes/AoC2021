from aocd import get_data
import re
import numpy as np

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

def increase(data):
    return data + 1

def flash_point(data, row, col):
    adj = data[row-1:row+2, col-1:col+2]
    adj = adj + 1
    continue_flashing = []
    for i in np.argwhere(adj > 9):
        ir = i[0]
        ic = i[1]
        if not (ir == row and ic == col):
            continue_flashing.append((ir + row - 1, ic + col-1))
    data[row-1:row+2, col-1:col+2] = adj
    return data, continue_flashing

def flash(data):
    to_flash = []
    already_flashed = set()
    for row in range(data.shape[0]):
        for col in range(data.shape[1]):
            if data[row][col] > 9:
                to_flash.append((row, col))

    num_flashes = 0
    while to_flash:
        nxt = to_flash.pop()
        already_flashed.add(nxt)
        data, continue_flashing = flash_point(data, nxt[0], nxt[1])
        continue_flashing = [i for i in continue_flashing if i not in already_flashed and i not in to_flash]
        to_flash += continue_flashing
        num_flashes += 1
    return data, num_flashes

def set_to_zero(data):
    data = np.where(data > 9, 0, data)
    return data

def parse_data(input_data):
    data = np.array([[int(i) for i in row] for row in input_data.split('\n')])
    return data

def run_game(data, num_rounds):
    total_flashes = 0
    for i in range(num_rounds):
        data = np.pad(data, 1, constant_values=(-10))
        data = increase(data)
        data, num_flashes = flash(data)
        total_flashes += num_flashes
        data = set_to_zero(data)
        data = data[1:-1,1:-1]
    return data, total_flashes

def part_one(input_data):
    data = parse_data(input_data)
    data, answer = run_game(data, num_rounds=20)
    print(answer)
    return data

def part_two(input_data):
    pass

data = part_one(test_data)