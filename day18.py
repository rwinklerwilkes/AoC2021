from aocd import get_data
import math
import re

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

def parse_data(input_data):
    lists = [eval(n) for n in input_data.split('\n')]
    return lists

def add_numbers(x, n, left_right):
    if n is None:
        return x
    elif isinstance(x, int):
        return x+n
    l, r = x
    if left_right == 'left':
        return [add_numbers(l, n, 'left'),r]
    elif left_right == 'right':
        return [l, add_numbers(r,n,'right')]

def split(c):
    if isinstance(c, int):
        if c >= 10:
            return True, [c//2, math.ceil(c/2)]
        else:
            return False, c
    else:
        a,b = c
        changed, a = split(a)
        if changed:
            return changed, [a,b]
        changed, b = split(b)
        return changed, [a, b]

def explode(c, depth=4):
    if isinstance(c, int):
        changed = False
        val = c
        left = None
        right = None
        return changed, val, left, right
    a,b = c
    if depth == 0:
        #we've gone at least 4 deep with recursion
        changed=True
        val=0
        left=a
        right=b
        return changed, val, left, right
    changed, a, left, right = explode(a, depth-1)
    if changed:
        changed=True
        #need to add the right number as far as possible to the left
        val= [a, add_numbers(b,right, 'left')]
        left = left
        right = None
        return changed, val, left, right

    changed, b, left, right = explode(b, depth - 1)
    if changed:
        changed=True
        #need to add the left number as far as possible to the right
        val= [add_numbers(a,left, 'right'),b]
        left = None
        right = right
        return changed, val, left, right

    changed = False
    val = c
    left = None
    right = None
    return changed, val, left, right


def add(a, b):
    c = [a, b]
    while True:
        changed, c, _, _ = explode(c)
        if changed:
            #continue to explode first
            continue
        changed, c = split(c)
        if not changed:
            break
    return c

def magnitude(c):
    if isinstance(c, int):
        return c
    else:
        a,b = c
        return 3*magnitude(a) + 2*magnitude(b)

def part_one(input_data):
    lists = parse_data(input_data)
    first = lists[0]
    rest = lists[1:]
    for c in rest:
        first = add(first, c)
    answer = magnitude(first)
    print(answer)

def part_two(input_data):
    lists = parse_data(input_data)
    max_val = 0
    for a in lists:
        for b in lists:
            if a != b:
                res = add(a, b)
                mag = magnitude(res)
                if mag > max_val:
                    max_val = mag

    print(max_val)

part_one(input_data)
part_two(input_data)