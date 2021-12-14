from aocd import get_data
import re
from collections import Counter, defaultdict

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def parse_data(input_data):
    template, rules = input_data.split('\n\n')
    rules_out = {}

    template_pairs = [template[i] + template[i + 1] for i in range(len(template) - 1)]
    template_pairs = Counter(template_pairs)

    for rule in rules.split('\n'):
        pre, ins = rule.split(' -> ')
        rules_out[pre] = ins

    return template, template_pairs, rules_out

def run_round(letters, template_pairs_counter, rules):
    new_template_pairs_counter = defaultdict(int)
    for pair, count in template_pairs_counter.items():
        new_letter = rules[pair]
        letters[new_letter] += count
        start_pair = pair[0] + new_letter
        end_pair = new_letter + pair[1]
        new_template_pairs_counter[start_pair] += count
        new_template_pairs_counter[end_pair] += count

    return letters, new_template_pairs_counter

def part_one(input_data):
    template_original, template_pairs_counter, rules = parse_data(input_data)
    letters = Counter(template_original)
    for i in range(10):
        letters, new_template_pairs_counter = run_round(letters, template_pairs_counter, rules)
        template_pairs_counter = new_template_pairs_counter

    counts = letters.values()
    answer = max(counts) - min(counts)
    print(answer)
    return letters

def part_two(input_data):
    template_original, template_pairs_counter, rules = parse_data(input_data)
    letters = Counter(template_original)
    for i in range(40):
        letters, new_template_pairs_counter = run_round(letters, template_pairs_counter, rules)
        template_pairs_counter = new_template_pairs_counter

    counts = letters.values()
    answer = max(counts) - min(counts)
    print(answer)
    return letters

_ = part_one(input_data)
_ = part_two(input_data)