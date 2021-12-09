from aocd import get_data
import re
import numpy as np

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

def parse_data(input_data):
    return np.array([[int(i) for i in row] for row in input_data.split('\n')])

def part_one(input_data):
    data = parse_data(input_data)
    low_spot_vals = []
    low_spots = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            up = np.inf
            left = np.inf
            down = np.inf
            right = np.inf
            val = data[i][j]
            if i > 0:
                up = data[i-1][j]
            if i < data.shape[0] - 1:
                down = data[i+1][j]
            if j > 0:
                left = data[i][j-1]
            if j < data.shape[1] - 1:
                right = data[i][j+1]
            if all([val<up, val<down, val<left, val<right]):
                low_spots.append((i,j))
                low_spot_vals.append(val)
    risk = [i+1 for i in low_spot_vals]
    print(sum(risk))
    return low_spots

def get_adjacent(shape, i, j):
    ret_list = []
    if i > 0:
        ret_list.append((i-1, j))
    if i < shape[0] - 1:
        ret_list.append((i+1, j))
    if j > 0:
        ret_list.append((i, j-1))
    if j < shape[1] - 1:
        ret_list.append((i, j + 1))
    return ret_list

def part_two(input_data, low_spots):
    data = parse_data(input_data)
    all_basins = {}
    for (i,j) in low_spots:
        basin_size = 0
        orig_i = i
        orig_j = j
        all_basins[(i,j)] = []
        to_visit = [(i,j)]
        visited = set()
        while to_visit:
            i,j = to_visit.pop()
            if (i,j) not in visited and data[i][j] != 9:
                basin_size += 1
                adjacent = get_adjacent(data.shape, i, j)
                to_visit += adjacent
                visited.add((i,j))
                all_basins[(orig_i,orig_j)].append((i,j))

    t = [len(v) for v in all_basins.values()]
    basin_sizes = sorted(t, reverse=True)
    biggest_three = basin_sizes[:3]
    print(np.prod(biggest_three))
    return all_basins


low_spots = part_one(input_data)
all_basins = part_two(input_data, low_spots)