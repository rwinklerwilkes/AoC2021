from aocd import get_data
import numpy as np

input_data = get_data(year=2021, day=1)
test_data = """199
200
208
210
200
207
240
269
260
263"""

def parse_data(input_data):
    return [int(i) for i in input_data.split('\n')]

def part_one(input_data):
    data = parse_data(input_data)
    last = None
    bigger_than_last = 0
    for i, val in enumerate(data):
        if last is None:
            last = val
        elif val > last:
            bigger_than_last += 1
        last = val
    print(bigger_than_last)

def part_two(input_data):
    data = parse_data(input_data)
    windows = np.lib.stride_tricks.sliding_window_view(data,3)
    window_sums = np.sum(windows,axis=1)
    last = None
    bigger_than_last = 0
    for i, val in enumerate(window_sums):
        if last is None:
            last = val
        elif val > last:
            bigger_than_last += 1
        last = val
    print(bigger_than_last)

part_one(input_data)
part_two(input_data)