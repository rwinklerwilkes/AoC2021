from aocd import get_data
import re

mx = r'^[a-zA-Z0-9\/:]*\/day([0-9]{1,}).py$'
day = int(re.match(mx, __file__).group(1))
input_data = get_data(year=2021, day=day)
test_packet = 'C200B40A82'

def to_bin(hex_packet):
    bin_pkt = bin(int(hex_packet, 16))[2:].zfill(len(hex_packet * 4))
    return bin_pkt

all_version = 0

def parse_packet(packet):
    global all_version
    version = int(packet[:3], 2)
    all_version += version
    tid = int(packet[3:6], 2)
    if tid == 4:
        i = 6
        while packet[i] == '1':
            i += 5
        i += 5
        packet = packet[i:]
    else:
        length_tid = packet[6]
        if length_tid == '0':
            length_in_bits = int(packet[7:22],2)
            subpackets = packet[22:22+length_in_bits]
            while subpackets:
                subpackets = parse_packet(subpackets)
            packet = packet[22+length_in_bits:]
        elif length_tid == '1':
            number_of_subpackets = int(packet[7:18],2)
            packet = packet[18:]
            for j in range(number_of_subpackets):
                packet = parse_packet(packet)
        # operator packet
    return packet

def parse_packet_part_two(packet):
    global all_version
    version = int(packet[:3], 2)
    all_version += version
    tid = int(packet[3:6], 2)
    if tid == 4:
        i = 6
        while packet[i] == '1':
            i += 5
        i += 5
        bits = packet[6:i]
        num = ''
        for b in range(len(bits) // 5):
            num += bits[5 * b + 1:5 * (b + 1)]
        literal_value = int(num, 2)
        return packet[i:], literal_value
    else:
        length_tid = packet[6]
        subpacket_vals = []
        if length_tid == '0':
            length_in_bits = int(packet[7:22],2)
            subpackets = packet[22:22+length_in_bits]
            while subpackets:
                spkt, subpkt_val = parse_packet_part_two(subpackets)
                subpackets = spkt
                subpacket_vals.append(subpkt_val)
            packet = packet[22+length_in_bits:]
        elif length_tid == '1':
            number_of_subpackets = int(packet[7:18],2)
            packet = packet[18:]
            for j in range(number_of_subpackets):
                spkt, subpkt_val = parse_packet_part_two(packet)
                packet = spkt
                subpacket_vals.append(subpkt_val)
        if tid == 0:
            return packet, sum(subpacket_vals)
        if tid == 1:
            array_mult = 1
            for s in subpacket_vals:
                array_mult *= s
            return packet, array_mult
        if tid == 2:
            return packet, min(subpacket_vals)
        if tid == 3:
            return packet, max(subpacket_vals)
        if tid == 5:
            assert len(subpacket_vals) == 2
            return packet, (subpacket_vals[0] > subpacket_vals[1])*1
        if tid == 6:
            assert len(subpacket_vals) == 2
            return packet, (subpacket_vals[0] < subpacket_vals[1]) * 1
        if tid == 7:
            assert len(subpacket_vals) == 2
            return packet, (subpacket_vals[0] == subpacket_vals[1]) * 1

def part_one(input_data):
    global all_version
    all_version = 0
    bin_packet = to_bin(input_data)
    parse_packet(bin_packet)
    print(all_version)

def part_two(input_data):
    global all_version
    all_version = 0
    bin_packet = to_bin(input_data)
    packet, value = parse_packet_part_two(bin_packet)
    print(packet)
    print(value)

part_one(input_data)
part_two(input_data)