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
    int_len = len(data[0])
    mode_vals = ''.join([str(c) for c in mode(data,axis=0).mode.flatten()])
    gamma = int(mode_vals, 2)
    epsilon_bin = np.binary_repr(np.invert(np.array(gamma,dtype=np.uint16)),width=16)[-int_len:]
    epsilon = int(epsilon_bin,2)
    print(gamma*epsilon)

def part_two(input_data):
    pass

part_one(input_data)