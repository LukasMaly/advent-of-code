#!/usr/bin/env python3

'''Day 3: Binary Diagnostic
https://adventofcode.com/2021/day/3
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, input: list[str]) -> int:
        occurences_of_one = self.get_ones_count(input)
        most_common = self.get_most_common(occurences_of_one, len(input))
        least_common = self.get_least_common(occurences_of_one, len(input))
        gamma_rate = int(''.join(most_common), 2)
        epsilon_rate = int(''.join(least_common), 2)
        return gamma_rate * epsilon_rate

    def part2(self, input: list[str]) -> int:
        oxygen_generator_rating = int(''.join(self.reduce_list(input[:], self.get_most_common)), 2)
        co2_scrubber_rating = int(''.join(self.reduce_list(input[:], self.get_least_common)), 2)
        return oxygen_generator_rating * co2_scrubber_rating

    def get_ones_count(self, input: list[str]) -> list[int]:
        return [int(sum(line[i] == '1' for line in input)) for i in range(len(input[0]))]

    def get_most_common(self, ones_count: list[int], length: int) -> list[str]:
        return ['1' if occurence >= length / 2 else '0' for occurence in ones_count]

    def get_least_common(self, ones_count: list[int], length: int) -> list[str]:
        return ['0' if occurence >= length / 2 else '1' for occurence in ones_count]

    def reduce_list(self, lines: list[str], common_func) -> str:
        for i in range(len(lines[0])):
            occurences_of_one = self.get_ones_count(lines)
            common = common_func(occurences_of_one, len(lines))
            lines = [line for line in lines if line[i] == common[i]]
            if len(lines) == 1:
                return lines[0]
        return ''


if __name__ == '__main__':
    Puzzle().run()
