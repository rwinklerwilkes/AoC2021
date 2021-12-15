from aocd import get_data
import re
import numpy as np
import heapq

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

def get_neighbors(vert):
    row, col = vert
    return [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]

def dijkstras(data, source):
    q = set()
    dist = {}
    prev = {}

    for row in range(data.shape[0]):
        for col in range(data.shape[1]):
            vert = (row, col)
            dist[vert] = np.inf
            prev[vert] = None
            q.add(vert)

    dist[source] = 0

    while q:
        dist_check = {k:v for k,v in dist.items() if k in q}
        sorted_dist = sorted(dist_check.items(), key=lambda x: x[1])
        u = sorted_dist[0][0]
        q.remove(u)
        neighbors = get_neighbors(u)
        for v in neighbors:
            if v in q:
                alt = dist[u] + data[v[0]][v[1]]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    return dist, prev

import itertools

class HQ:
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.REMOVED = '<removed-task>'
        self.counter = itertools.count()

    def push(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task, priority
        raise KeyError('pop from an empty priority queue')


def dijkstras_heapq(data, source):
    q = HQ()
    dist = {source:0}
    prev = {}
    for row in range(data.shape[0]):
        for col in range(data.shape[1]):
            vert = (row, col)
            if vert != source:
                dist[vert] = 10000000
                prev[vert] = None

            q.push(vert, dist[vert])

    try:
        while len(q.pq) > 0:
            u, _ = q.pop()
            neighbors = get_neighbors(u)
            neighbors = [n for n in neighbors if n in q.entry_finder.keys()]
            for v in neighbors:
                alt = dist[u] + data[v[0]][v[1]]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    q.push(v, alt)
    except KeyError as k:
        print('Done')
    return dist, prev


def parse_data(input_data):
    return np.array([[int(i) for i in row] for row in input_data.split('\n')])

def generate_map_part_two(data):
    new_full_map = np.tile(data,(5,5))
    orig_rows = data.shape[0]
    orig_cols = data.shape[1]
    for row in range(new_full_map.shape[0]):
        for col in range(new_full_map.shape[1]):
            rowsum = row//orig_rows
            colsum = col//orig_cols
            new_full_map[row][col] += rowsum + colsum
            if new_full_map[row][col] >= 10:
                new_full_map[row][col] -= 9
    return new_full_map

def part_one(input_data):
    data = parse_data(input_data)
    dist, prev = dijkstras_heapq(data, (0,0))
    dest_row = data.shape[0]-1
    dest_col = data.shape[1]-1
    answer = dist[(dest_row,dest_col)]
    print(answer)

def part_two(input_data):
    data = parse_data(input_data)
    data = generate_map_part_two(data)
    dist, prev = dijkstras_heapq(data, (0,0))
    dest_row = data.shape[0]-1
    dest_col = data.shape[1]-1
    answer = dist[(dest_row,dest_col)]
    print(answer)


part_one(input_data)
part_two(input_data)