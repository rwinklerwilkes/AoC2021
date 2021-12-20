from aocd import get_data
import re
import numpy as np
from scipy import ndimage as ndi

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""

def parse_data(input_data):
    lines = input_data.split('\n\n')
    enhance_algo = lines[0].replace('\n', '')
    enhance_algo = np.array([i for i, c in enumerate(enhance_algo) if c == '#'])
    board_list = lines[1].split('\n')
    bin_board = []
    for i, row in enumerate(board_list):
        bin_board.append([])
        for j, col in enumerate(row):
            bin_board[i].append((col == '#')*1)
    img = np.array(bin_board)
    img = np.pad(img, ((50,50), (50, 50)))

    kernel = np.array([[1,2,4], [8,16,32], [64,128,256]])

    return enhance_algo, img, kernel

def part_one(input_data):
    enhance_algo, img, kernel = parse_data(input_data)
    num_rounds = 2
    new_img = img.copy()
    for i in range(num_rounds):
        new_img = ndi.convolve(new_img, weights=kernel, mode="constant", cval = i%2)
        new_img = np.isin(new_img, enhance_algo)*1

    print(new_img.sum())

def part_two(input_data):
    enhance_algo, img, kernel = parse_data(input_data)
    num_rounds = 50
    new_img = img.copy()
    for i in range(num_rounds):
        new_img = ndi.convolve(new_img, weights=kernel, mode="constant", cval = i%2)
        new_img = np.isin(new_img, enhance_algo)*1

    print(new_img.sum())

part_one(input_data)
part_two(input_data)