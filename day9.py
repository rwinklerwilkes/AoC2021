from aocd import get_data
import re

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)

def part_one(input_data):
    pass

def part_two(input_data):
    pass