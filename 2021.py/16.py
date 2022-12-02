#!/usr/bin/env python3

'''Day 16: Packet Decoder
https://adventofcode.com/2021/day/16
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        bits = self.parse_input(lines)
        packet, _ = self.parse_packet(bits)
        return self.count_version_sum(packet)

    def part2(self, lines: list[str]) -> int:
        bits = self.parse_input(lines)
        packet, _ = self.parse_packet(bits)
        return self.calculate_value(packet) 

    def parse_input(self, lines: list[str]) -> str:
        return bin(int(lines[0], 16))[2:].zfill(len(lines[0] * 4))

    def parse_packet(self, bits: str, ptr: int = 0) -> tuple[dict[str, int], int]:
        packet = {}
        packet['version'] = int(bits[ptr:ptr+3], base=2)
        ptr += 3
        packet['type_id'] = int(bits[ptr:ptr+3], base=2)
        ptr += 3
        packet['subpackets'] = []
        if packet['type_id'] == 4:  # literal value
            groups = []
            packet_end = False
            while not packet_end:
                if bits[ptr] == '0':
                    packet_end = True
                ptr += 1
                groups.append(bits[ptr:ptr+4])
                ptr += 4
            packet['value'] = int(''.join(groups), 2)
        else:  # operator
            length_type_id = int(bits[ptr], base=2)
            ptr += 1
            if length_type_id == 0:
                total_length = int(bits[ptr:ptr+15], base=2)
                ptr += 15
                subpackets_end = ptr + total_length
                while ptr != subpackets_end:
                    subpacket, ptr = self.parse_packet(bits, ptr)
                    packet['subpackets'].append(subpacket)
            elif length_type_id == 1:
                number_of_subpackets = int(bits[ptr:ptr+11], base=2)
                ptr += 11
                for i in range(number_of_subpackets):
                    subpacket, ptr = self.parse_packet(bits, ptr)
                    packet['subpackets'].append(subpacket)
        return packet, ptr

    def count_version_sum(self, packet, version_sum=0) -> int:
        version_sum += packet['version']
        for subpacket in packet['subpackets']:
            version_sum = self.count_version_sum(subpacket, version_sum)
        return version_sum

    def calculate_value(self, packet: dict[str, int], value=0) -> int:
        if packet['type_id'] == 4:
            return packet['value']
        else:
            values = [self.calculate_value(packet) for packet in packet['subpackets']]
            if packet['type_id'] == 0:
                return sum(values)
            elif packet['type_id'] == 1:
                product = 1
                for value in values:
                    product *= value
                return product
            elif packet['type_id'] == 2:
                return min(values)
            elif packet['type_id'] == 3:
                return max(values)
            elif packet['type_id'] == 5:
                return int(values[0] > values[1])
            elif packet['type_id'] == 6:
                return int(values[0] < values[1])
            else:  # packet['type_id'] == 7
                return int(values[0] == values[1])


if __name__ == '__main__':
    Puzzle().run()
