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

def part_two(input_data):
    data = parse_data(input_data)
    common_vals = ''.join([str(c) for c in mode(data,axis=0).mode.flatten()])

    generator = None
    position = 0
    while generator is None:
        pass

    scrubber = None
    position = 0
    while scrubber is None:
        pass

part_one(input_data)