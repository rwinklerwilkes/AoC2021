from aocd import get_data
import re
import numpy as np

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)

def get_rotations():
    all_vectors = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    all_vectors = [np.array(i) for i in all_vectors]
    all_rotations = []
    for vi in all_vectors:
        for vj in all_vectors:
            d = np.dot(vi, vj)
            if d == 0:
                vk = np.cross(vi, vj)
                all_rotations.append(np.array([vi, vj, vk]))
    return np.array(all_rotations)


def part_one(input_data):
    pass

def part_two(input_data):
    pass