from aocd import get_data
import re
import numpy as np

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """16,1,2,0,4,2,7,1,2,14"""

def check_fuel_cost(input_data, target_val):
    cost = np.sum(np.abs(input_data - target_val))
    return cost

def check_fuel_cost_part_two(input_data, target_val):
    prelim_cost = np.abs(input_data - target_val)
    actual_cost = (prelim_cost*(prelim_cost+1))/2
    cost = np.sum(actual_cost)
    return cost

def parse_data(input_data):
    return np.array([int(i) for i in input_data.split(',')])

def part_one(input_data):
    data = parse_data(input_data)
    min_cost = np.inf
    for i in range(np.min(data), np.max(data)+1):
        cost = check_fuel_cost(data, i)
        if cost < min_cost:
            min_cost = cost
    print(min_cost)


def part_two(input_data):
    data = parse_data(input_data)
    min_cost = np.inf
    for i in range(np.min(data), np.max(data)+1):
        cost = check_fuel_cost_part_two(data, i)
        if cost < min_cost:
            min_cost = cost
    print(min_cost)

part_one(input_data)
part_two(input_data)