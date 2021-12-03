from aocd import get_data
import re
import numpy as np
from scipy.stats import mode

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

def parse_data(input_data):
    return [[int(c) for c in row] for row in input_data.split('\n')]

def part_one(input_data):
    data = parse_data(input_data)
    most_common = [np.argmax(np.bincount(row)) for row in np.array(data).T]
    gamma_vals = ''.join([str(c) for c in most_common])
    gamma = int(gamma_vals, 2)
    least_common = [np.argmin(np.bincount(row)) for row in np.array(data).T]
    epsilon_vals = ''.join([str(c) for c in least_common])
    epsilon = int(epsilon_vals,2)
    print(gamma*epsilon)

def find_generator(data):
    generator = None
    position = 0

    data_to_check = data.T[position, :]
    data_keep = data
    while generator is None:
        counts = np.bincount(data_to_check)
        if counts[0] == counts[1]:
            keep_val = 1
        else:
            keep_val = np.argmax(counts)

        data_keep = data_keep[np.where(data_to_check==keep_val),:][0]
        if data_keep.shape[0] == 1:
            generator_vals = ''.join([str(c) for c in data_keep[0]])
            generator = int(generator_vals, 2)
            break
        position += 1
        data_to_check = data_keep.T[position,:]
        keep_val = None

    return generator

def find_scrubber(data):
    scrubber = None
    position = 0
    data_to_check = data.T[position, :]
    data_keep = data
    while scrubber is None:
        counts = np.bincount(data_to_check)
        if counts[0] == counts[1]:
            keep_val = 0
        else:
            keep_val = np.argmin(counts)

        data_keep = data_keep[np.where(data_to_check==keep_val),:][0]
        if data_keep.shape[0] == 1:
            scrubber_vals = ''.join([str(c) for c in data_keep[0]])
            scrubber = int(scrubber_vals, 2)
            break
        position += 1
        data_to_check = data_keep.T[position, :]
        keep_val = None

    return scrubber

def part_two(input_data):
    data = parse_data(input_data)
    data = np.array(data)

    generator = find_generator(data)
    scrubber = find_scrubber(data)
    print(generator*scrubber)


part_one(input_data)
part_two(input_data)