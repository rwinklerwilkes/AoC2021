from aocd import get_data
import re
import numpy as np

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)

test_data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

def parse_data(input_data):
    dt, inst = input_data.split('\n\n')
    dots = dt.split('\n')
    dots_out = set()
    for dot in dots:
        x, y = dot.split(',')
        dots_out.add((int(x), int(y)))
    fold_inst = inst.split('\n')
    return dots_out, fold_inst


def parse_inst(inst):
    re_x = r'^fold along x=([0-9]{1,})$'
    re_y = r'^fold along y=([0-9]{1,})$'
    match_x = re.match(re_x, inst)
    match_y = re.match(re_y, inst)
    func = None
    val = None
    if match_x:
        func = fold_horiz
        val = int(match_x.group(1))
    elif match_y:
        func = fold_vert
        val = int(match_y.group(1))
    return func, val

def fold_horiz(dots, x):
    new_dots = set()
    for dtx, dty in dots:
        if dtx < x:
            new_dots.add((dtx, dty))
        else:
            md = dtx%(x+1)
            new_x = (x-1) - md
            new_dots.add((new_x, dty))
    return new_dots

def fold_vert(dots, y):
    new_dots = set()
    for dtx, dty in dots:
        if dty < y:
            new_dots.add((dtx, dty))
        else:
            md = dty%(y+1)
            new_y = (y-1) - md
            new_dots.add((dtx, new_y))
    return new_dots

def plot_board(dots):
    max_x = max([x for x,y in dots])+1
    max_y = max([y for x,y in dots])+1
    empty = [['.' for col in range(max_x)] for row in range(max_y)]
    for x,y in dots:
        empty[y][x] = '#'
    outstr = ''
    for row in empty:
        outstr += ''.join(row)
        outstr += '\n'
    print(outstr)

def part_one(input_data):
    dots, inst = parse_data(input_data)
    func, val = parse_inst(inst[0])
    new_dots = func(dots, val)
    answer = len(new_dots)
    print(answer)

def part_two(input_data):
    dots, inst = parse_data(input_data)
    for instruction in inst:
        func, val = parse_inst(instruction)
        new_dots = func(dots, val)
        dots = new_dots
    plot_board(dots)

# part_one(input_data)
part_two(input_data)