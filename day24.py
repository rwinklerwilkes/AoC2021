from aocd import get_data
import re
from collections import defaultdict

input_data = get_data(year=2021, day=24)

#Lots of help from https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hps5hgw/?utm_source=share&utm_medium=web2x&context=3

test_data = """inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2"""

class ALU:
    def __init__(self):
        self.reset()

    def reset(self):
        self.storage = defaultdict(int)
        self.num_input = 0

    def set_storage(self, a, input):
        self.storage[a] = input[self.num_input]
        self.num_input += 1

    def int_or_var(self, var):
        regex = '-{0,1}[0-9]{1,}'
        if re.match(regex, var):
            return 'int', int(var)
        else:
            return 'var', self.storage[var]

    def add(self, a, b):
        b_type, b = self.int_or_var(b)
        self.storage[a] = self.storage[a] + b

    def mul(self, a, b):
        b_type, b = self.int_or_var(b)
        self.storage[a] = self.storage[a] * b

    def div(self, a, b):
        b_type, b = self.int_or_var(b)
        if b == 0:
            pass
        else:
            self.storage[a] = self.storage[a] // b

    def mod(self, a, b):
        b_type, b = self.int_or_var(b)
        if self.storage[a] < 0 or b <= 0:
            pass
        else:
            self.storage[a] = self.storage[a] % b

    def eql(self, a, b):
        b_type, b = self.int_or_var(b)

        if self.storage[a]==b:
            store_val = 1
        else:
            store_val = 0
        self.storage[a] = store_val

    def parse_instruction(self, instruction):
        match instruction.split(' '):
            case ['inp', a]:
                return lambda x: self.set_storage(a, x)
            case ['add', a, b]:
                return lambda x: self.add(a, b)
            case ['mul', a, b]:
                return lambda x: self.mul(a, b)
            case ['div', a, b]:
                return lambda x: self.div(a, b)
            case ['mod', a, b]:
                return lambda x: self.mod(a, b)
            case ['eql', a, b]:
                return lambda x: self.eql(a, b)

    def parse_program(self, instructions):
        all_instructions = instructions.split('\n')
        check_inst = instructions.split('\n')[0]
        assert check_inst.split(' ')[0] == 'inp'

        i = 0
        program = []
        for i, inst in enumerate(all_instructions):
            program.append(self.parse_instruction(inst))

        return program

    def run_program_2(self, instructions, input):
        self.reset()
        all_instructions = instructions.split('\n')
        for i, inst in enumerate(all_instructions):
            pi = self.parse_instruction(inst)
            if inst.split(' ')[0] == 'inp':
                pass
            pi(input)

    def run_program(self, program, input):
        self.reset()
        for inst in program:
            inst(input)

def part_one(input_data):
    input_test = [int(i) for i in '45989929946199']
    alu = ALU()
    program = alu.parse_program(input_data)
    alu.run_program_2(input_data, input_test)
    result = alu.storage['z']
    if result == 0:
        # valid
        print('Valid')
    elif result != 0:
        # invalid
        print(f'Invalid, {result}')

def part_two(input_data):
    input_test = [int(i) for i in '11912814611156']
    alu = ALU()
    program = alu.parse_program(input_data)
    alu.run_program_2(input_data, input_test)
    result = alu.storage['z']
    if result == 0:
        # valid
        print('Valid')
    elif result != 0:
        # invalid
        print(f'Invalid, {result}')

part_one(input_data)
part_two(input_data)