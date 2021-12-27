from aocd import get_data
import re

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)

def part_one(input_data):
    # Manually completed with use of https://amphipod.net/
    # https://www.reddit.com/r/adventofcode/comments/rmu3bo/2021_day_23_interactive_solver_web_app/
    pass

def part_two(input_data):
    # Manually completed with use of https://amphipod.net/
    # https://www.reddit.com/r/adventofcode/comments/rmu3bo/2021_day_23_interactive_solver_web_app/
    pass