from aocd import get_data
import re
import numpy as np

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

def check_line(line):
    stack = []
    closing = {')':'(',
               '>':'<',
               '}':'{',
               ']':'['}
    points = {')':3,']':57,'}':1197,'>':25137}
    valid = True
    total = 0
    for char in line:
        if char in closing.values():
            stack.append(char)
        elif char in closing.keys():
            last_char = stack.pop()
            if closing[char] != last_char:
                valid = False
                total += points[char]
    return valid, total

def check_line_part_two(line):
    stack = []
    closing = {')':'(',
               '>':'<',
               '}':'{',
               ']':'['}
    opening = {v:k for k,v in closing.items()}
    points = {')':1,']':2,'}':3,'>':4}
    valid = True

    for char in line:
        if char in closing.values():
            stack.append(char)
        elif char in closing.keys():
            last_char = stack.pop()
            if closing[char] != last_char:
                valid = False

    finish_str = ''
    total = 0
    if valid and len(stack) != 0:
        finish_str = ''
        total = 0
        while stack:
            total *= 5
            next_chr = opening[stack.pop()]
            total += points[next_chr]
            finish_str += next_chr
    return finish_str, total


def part_one(input_data):
    data_lines = input_data.split('\n')
    sum_total = 0
    for line in data_lines:
        valid, total = check_line(line)
        sum_total += total
    print(sum_total)

def part_two(input_data):
    data_lines = input_data.split('\n')
    all_lines = []
    for line in data_lines:
        finish_str, total = check_line_part_two(line)
        if total > 0:
            all_lines.append(total)
    print(np.median(all_lines))

part_one(input_data)
part_two(input_data)