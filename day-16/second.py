import math
from enum import Enum


class OperatorLengthTypeId(Enum):
    TOTAL_LENGTH = 0
    NUM_OF_SUB_PACKETS = 1


class PacketType(Enum):
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL = 7


def read_packet_type(packet):
    return PacketType(int(packet[3:6], 2))


def read_packet_version(packet):
    return int(packet[:3], 2)


def convert_to_binary(current_packet):
    return bin(int(current_packet, 16))[2:].zfill(len(current_packet) * 4)


def read_operator_length_type_id(packet):
    return OperatorLengthTypeId(int(packet[6]))


def read_operator_total_length(packet):
    return int(packet[7:22], 2)


def read_literal_length(packet):
    length = 6
    i = 0
    while packet[i * 5 + 6] == '1':
        length += 5
        i += 1
    return length + 5


def read_operator_num_of_sub_packets(packet):
    return int(packet[7:18], 2)


def read_literal(packet):
    length = read_literal_length(packet)
    current = 6
    number = ""
    while current < length:
        number += packet[current + 1:current + 5]
        current += 5
    return int(number, 2)


def parse_packet(packet):
    packet_type = read_packet_type(packet)
    if packet_type == PacketType.LITERAL:
        return read_literal(packet), read_literal_length(packet)
    packet_length = 7
    length_type = read_operator_length_type_id(packet)
    results = []
    if length_type == OperatorLengthTypeId.TOTAL_LENGTH:
        packet_length += 15
        total_length = read_operator_total_length(packet)
        sub_packets = packet[22:]
        current_length = 0
        while current_length != total_length:
            result, sub_length = parse_packet(sub_packets)
            results.append(result)
            packet_length += sub_length
            current_length += sub_length
            sub_packets = sub_packets[sub_length:]
    else:
        packet_length += 11
        num_of_sub_packets = read_operator_num_of_sub_packets(packet)
        sub_packets = packet[18:]
        for i in range(num_of_sub_packets):
            result, sub_length = parse_packet(sub_packets)
            results.append(result)
            packet_length += sub_length
            sub_packets = sub_packets[sub_length:]
    result = 0
    if packet_type == PacketType.SUM:
        result = sum(results)
    elif packet_type == PacketType.PRODUCT:
        result = math.prod(results)
    elif packet_type == PacketType.MINIMUM:
        result = min(results)
    elif packet_type == PacketType.MAXIMUM:
        result = max(results)
    elif packet_type == PacketType.GREATER_THAN:
        result = int(results[0] > results[1])
    elif packet_type == PacketType.LESS_THAN:
        result = int(results[0] < results[1])
    elif packet_type == PacketType.EQUAL:
        result = int(results[0] == results[1])
    return result, packet_length


def main():
    packet = open("input.txt", "r").readline().strip()
    packet = convert_to_binary(packet)
    result, _ = parse_packet(packet)
    print(result)


if __name__ == '__main__':
    main()
