#!/usr/bin/env python3

'''Day 3: Binary Diagnostic
https://adventofcode.com/2021/day/3
'''

from typing import List
from utils import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self) -> None:
        super().__init__()

    def part1(self, input: List[str]) -> int:
        occurences_of_one = self.get_ones_count(input)
        most_common = self.get_most_common(occurences_of_one, len(input))
        least_common = self.get_least_common(occurences_of_one, len(input))
        gamma_rate = int(''.join(most_common), 2)
        epsilon_rate = int(''.join(least_common), 2)
        return gamma_rate * epsilon_rate

    def part2(self, input: List[str]) -> int:
        oxygen_generator_rating = int(''.join(self.reduce_list(input, self.get_most_common)), 2)
        co2_scrubber_rating = int(''.join(self.reduce_list(input, self.get_least_common)), 2)
        return oxygen_generator_rating * co2_scrubber_rating

    def get_ones_count(self, lines: List[str]) -> List[int]:
        ones_count = [0] * len(lines[0])
        for line in lines:
            for i, character in enumerate(line):
                ones_count[i] += int(character)
        return ones_count

    def get_most_common(self, ones_count: List[int], length: int) -> List[str]:
        return ['1' if occurence >= length / 2 else '0' for occurence in ones_count]

    def get_least_common(self, ones_count: List[int], length: int) -> List[str]:
        return['0' if occurence >= length / 2 else '1' for occurence in ones_count]

    def reduce_list(self, lines: List[str], commonnes_function) -> str:
        reduced_list = lines.copy()
        for i in range(len(lines[0])):
            occurences_of_one = self.get_ones_count(reduced_list)
            commonness = commonnes_function(occurences_of_one, len(reduced_list))
            reduced_list = [line for line in reduced_list if line[i] == commonness[i]]
            if len(reduced_list) == 1:
                return reduced_list[0]
        return ''


if __name__ == '__main__':
    Puzzle().run()
