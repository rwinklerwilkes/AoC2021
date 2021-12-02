from aocd import get_data
import re

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def parse_instruction(instruction):
    fx = r'forward ([0-9]{1,})'
    dx = r'down ([0-9]{1,})'
    ux = r'up ([0-9]{1,})'
    if re.match(fx, instruction):
        retval = [int(re.match(fx, instruction).group(1)),0]
    elif re.match(dx, instruction):
        retval = [0,int(re.match(dx, instruction).group(1))]
    elif re.match(ux, instruction):
        retval = [0, -int(re.match(ux, instruction).group(1))]
    return retval

def part_one(input_data):
    horizontal = 0
    depth = 0
    for instruction in input_data.split('\n'):
        hz, dp = parse_instruction(instruction)
        horizontal += hz
        depth += dp

    print(horizontal*depth)


def part_two(input_data):
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in input_data.split('\n'):
        hz, am = parse_instruction(instruction)
        if hz:
            horizontal += hz
            depth += hz*aim
        if am:
            aim += am

    print(horizontal*depth)


part_one(input_data)
part_two(input_data)