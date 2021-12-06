from aocd import get_data
import re
from collections import Counter

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = '3,4,3,1,2'

def parse_data(input_data):
    return [int(i) for i in input_data.split(',')]

def part_one(input_data):
    data = parse_data(input_data)
    num_days = 80
    next_day = Counter(data)
    for i in range(num_days):
        next_day = {days_left-1: count for days_left, count in next_day.items()}
        if -1 in next_day:
            reset_existing = next_day.get(6, 0) + next_day[-1]
            create_new = next_day.get(8,0) + next_day[-1]
            next_day[6] = reset_existing
            next_day[8] = create_new
            del next_day[-1]
    total_pop = [v for k,v in next_day.items()]
    print(sum(total_pop))


def part_two(input_data):
    data = parse_data(input_data)
    num_days = 256
    next_day = Counter(data)
    for i in range(num_days):
        next_day = {days_left-1: count for days_left, count in next_day.items()}
        if -1 in next_day:
            reset_existing = next_day.get(6, 0) + next_day[-1]
            create_new = next_day.get(8,0) + next_day[-1]
            next_day[6] = reset_existing
            next_day[8] = create_new
            del next_day[-1]
    total_pop = [v for k,v in next_day.items()]
    print(sum(total_pop))

part_one(input_data)
part_two(input_data)