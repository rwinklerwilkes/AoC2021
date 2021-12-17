from aocd import get_data
import re
import math

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)

def get_position(initial_velocity, t, initial_position=(0,0)):
    vx0, vy0 = initial_velocity
    x0, y0 = initial_position
    if vx0 > 0:
        drag = [min(vx0, i) for i in range(t)]
    elif vx0 < 0:
        drag = [max(vx0, -i) for i in range(t)]
    else:
        drag = 0
    x = x0 + t*vx0 - sum(drag)
    y = y0 + vy0 * t - (t*(t-1))/2
    return x, y

def get_velocity(initial_velocity, t):
    vx0, vy0 = initial_velocity
    if vx0 > 0:
        vx = vx0-min(vx0, t)
    elif vx0 < 0:
        vx = vx0-max(vx0,-t)
    else:
        vx = 0
    vy = vy0 - t
    return vx, vy

def check_target(tx_limits, ty_limits, initial_velocity, t):
    x,y = get_position(initial_velocity=initial_velocity, t=t)
    if x >= tx_limits[0] and x <= tx_limits[1] and y >= ty_limits[0] and y <= ty_limits[1]:
        return x,y, True
    else:
        return x,y, False

def check_hit(tx_limits, ty_limits, initial_velocity):
    any_hits = False
    pos_x = 0
    pos_y = 0
    i = 0
    while pos_x <= tx_limits[1] or pos_y >= ty_limits[1]:
        pos_x, pos_y, hit_this_time = check_target(tx_limits, ty_limits, initial_velocity, i)
        if hit_this_time:
            any_hits = True
        i += 1
    return any_hits

def part_one(input_data):
    pass

def part_two(input_data):
    pass