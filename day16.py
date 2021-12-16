from aocd import get_data
import re

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)

def parse_literal(packet):
    pass

def parse_packet(packet):
    bin_pkt = bin(int(packet, 16))[2:]
    version = int(bin_pkt[:3], 2)
    tid = int(bin_pkt[3:6], 2)
    if tid == 4:
        i = 6
        while bin_pkt[i] == '1':
            i += 5
        i += 5
        bits = bin_pkt[6:i]
        num = ''
        for i in range(len(bits)//5):
            num += bits[5*i+1:5*(i+1)]
        value = int(num,2)
    else:
        length_tid = bin_pkt[6]
        if length_tid == 0:
            length_in_bits = int(bin_pkt[7:22],2)

        elif length_tid == 1:
            number_of_subpackets = int(bin_pkt[7:18],2)
        # operator packet

def part_one(input_data):
    pass

def part_two(input_data):
    pass