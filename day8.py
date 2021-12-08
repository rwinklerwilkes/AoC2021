from aocd import get_data
import re

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

def digits_definition():
    digits = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    overlaps = {}
    for num, d in enumerate(digits):
        one_overlap = len([i for i in d if i in digits[1]])
        four_overlap = len([i for i in d if i in digits[4]])
        overlaps[f'{one_overlap}{four_overlap}{len(d)}'] = num
    return digits, overlaps

def parse_data(input_data):
    out = []
    for i in input_data.split('\n'):
        sp = i.split(' | ')
        signal_patterns = sp[0].split(' ')
        output_values = sp[1].split(' ')
        out.append((signal_patterns, output_values))
    return out

def part_one(input_data):
    digits, _ = digits_definition()
    digits_count = [len(l) for l in digits]
    input_parsed = parse_data(input_data)
    check_digits = [1,4,7,8]
    check_digits_counts = [digits_count[i] for i in check_digits]
    counter = 0
    for signal_patterns, output_values in input_parsed:
        ovlen = [l for l in output_values if len(l) in check_digits_counts]
        counter += len(ovlen)
    print(counter)

def determine_mapping(signal_patterns):
    _, overlaps = digits_definition()
    lengths = {len(l): l for l in signal_patterns}
    #one, four, seven each have unique lengths and their overlap with each digit along with each digit length uniquely
    #determines which number each string represents
    check_overlap = [lengths[2],lengths[4]]
    mapping = {}
    for s in signal_patterns:
        if s not in mapping:
            one_overlap = len([i for i in s if i in check_overlap[0]])
            four_overlap = len([i for i in s if i in check_overlap[1]])
            check_string = f'{one_overlap}{four_overlap}{len(s)}'
            mapping[''.join(sorted(s))] = overlaps[check_string]
    return mapping



def part_two(input_data):
    input_parsed = parse_data(input_data)
    total = 0
    for signal_patterns, output_values in input_parsed:
        add_str = ''
        mapping = determine_mapping(signal_patterns)
        for o in output_values:
            check_map = ''.join(sorted(o))
            add_str += str(mapping[check_map])
        total += int(add_str)
    print(total)



part_one(input_data)
part_two(input_data)