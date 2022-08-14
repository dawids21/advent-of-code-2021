from enum import Enum


class OperatorLengthTypeId(Enum):
    TOTAL_LENGTH = 0
    NUM_OF_SUB_PACKETS = 1


def read_packet_version(packet):
    return int(packet[:3], 2)


def is_operator(packet):
    return int(packet[3:6], 2) != 4


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


def parse_packet(packet):
    sum_of_versions = read_packet_version(packet)
    if not is_operator(packet):
        return sum_of_versions, read_literal_length(packet)
    packet_length = 7
    length_type = read_operator_length_type_id(packet)
    if length_type == OperatorLengthTypeId.TOTAL_LENGTH:
        packet_length += 15
        total_length = read_operator_total_length(packet)
        sub_packets = packet[22:]
        current_length = 0
        while current_length != total_length:
            sum_of_sub_versions, sub_length = parse_packet(sub_packets)
            sum_of_versions += sum_of_sub_versions
            packet_length += sub_length
            current_length += sub_length
            sub_packets = sub_packets[sub_length:]
    else:
        packet_length += 11
        num_of_sub_packets = read_operator_num_of_sub_packets(packet)
        sub_packets = packet[18:]
        for i in range(num_of_sub_packets):
            sum_of_sub_versions, sub_length = parse_packet(sub_packets)
            sum_of_versions += sum_of_sub_versions
            packet_length += sub_length
            sub_packets = sub_packets[sub_length:]
    return sum_of_versions, packet_length


def main():
    packet = open("input.txt", "r").readline().strip()
    packet = convert_to_binary(packet)
    sum_of_versions, packet_length = parse_packet(packet)
    print(sum_of_versions, packet_length)


if __name__ == '__main__':
    main()
