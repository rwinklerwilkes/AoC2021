from aocd import get_data
import re

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """target area: x=20..30, y=-10..-5"""

def parse_data(input_data):
    area_regex = r'target area: x=(\-{0,1}[0-9]{1,})..(\-{0,1}[0-9]{1,}), y=(\-{0,1}[0-9]{1,})..(\-{0,1}[0-9]{1,})'
    mobj = re.match(area_regex, input_data)
    tx_limits = [int(mobj.group(1)), int(mobj.group(2))]
    ty_limits = [int(mobj.group(3)), int(mobj.group(4))]
    return tx_limits, ty_limits

def get_position(initial_velocity, t, initial_position=(0,0)):
    vx0, vy0 = initial_velocity
    x0, y0 = initial_position
    if vx0 > 0:
        drag = [min(vx0, i) for i in range(t)]
    elif vx0 < 0:
        drag = [max(vx0, -i) for i in range(t)]
    else:
        drag = [0]
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
    max_y = pos_y
    mx = max(tx_limits)
    my = min(ty_limits)
    while pos_x <= mx and pos_y >= my:
        pos_x, pos_y, hit_this_time = check_target(tx_limits, ty_limits, initial_velocity, i)
        if pos_y > max_y:
            max_y = pos_y
        if hit_this_time:
            any_hits = True
        i += 1
    return any_hits, max_y

def part_one(input_data):
    tx_limits, ty_limits = parse_data(input_data)
    max_y = 0
    for initx in range(1,50):
        for inity in range(1,300):
            any_hit, max_y_this_time = check_hit(tx_limits, ty_limits, (initx, inity))
            if any_hit and max_y_this_time > max_y:
                max_y = max_y_this_time
    print(max_y)

def part_two(input_data):
    tx_limits, ty_limits = parse_data(input_data)
    sum_hits = 0
    for initx in range(0, 150):
        for inity in range(-200, 300):
            any_hit, _ = check_hit(tx_limits, ty_limits, (initx, inity))
            if any_hit:
                sum_hits += 1
    print(sum_hits)

# part_one(input_data)
# hits = part_two(test_data)
part_two(input_data)