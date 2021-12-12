from aocd import get_data
from collections import defaultdict
import re

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


def parse_data(input_data):
    adj = defaultdict(set)
    for edge in input_data.split('\n'):
        n0, n1 = edge.split('-')
        adj[n0].add(n1)
        adj[n1].add(n0)
    return adj


def pathfind(node, already_seen, adj):
    # If we've reach the end of the cave, return 1
    if node == 'end':
        return 1
    # If we've already visited this place, this isn't a valid path, so return 0
    if node.islower() and node in already_seen:
        return 0
    paths_here = 0
    # Add this node to the list of places we've already visited
    already_seen = already_seen.union({node})
    for nbr in adj[node]:
        # For each of the neighbors, count the number of ways to get to the end through those neighbors while passing
        # through all of the places we've already visited
        paths_here += pathfind(nbr, already_seen, adj)
    return paths_here


def pathfind_part_two(node, already_seen, adj, revisited=None):
    # If we've reach the end of the cave, return 1
    if node == 'end':
        return 1
    # If we get back to the start but we've gone somewhere else, this is invalid - we can only visit the start once
    if node == 'start' and len(already_seen) > 0:
        return 0
    # If we visit a small room and we this is a revisit, but we haven't done any other revisits, revisit here and
    # continue on as normal. Otherwise, this isn't a valid path and we return 0
    if node.islower() and node in already_seen:
        if revisited is None:
            revisited = node
        else:
            return 0
    # Continue on as in part 1, counting the number of ways to get to the end through their neighbors while passing
    # through the places we've already passed through.
    paths_here = 0
    already_seen = already_seen.union({node})
    for nbr in adj[node]:
        paths_here += pathfind_part_two(nbr, already_seen, adj, revisited)
    return paths_here


def part_one(input_data):
    adj = parse_data(input_data)
    answer = pathfind('start', set(), adj=adj)
    print(answer)


def part_two(input_data):
    adj = parse_data(input_data)
    answer = pathfind_part_two('start', set(), adj=adj)
    print(answer)


part_one(input_data)
part_two(input_data)
