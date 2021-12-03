#!/usr/bin/env python3

'''Day 3: Binary Diagnostic
https://adventofcode.com/2021/day/3
'''

from typing import List, Tuple


def read_input() -> List[str]:
    with open('inputs/day03.txt') as f:
        return f.read().splitlines()


def get_ones_count(lines: List[str]) -> List[int]:
    ones_count = [0] * len(lines[0])
    for line in lines:
        for i, character in enumerate(line):
            ones_count[i] += int(character)
    return ones_count


def get_most_common(ones_count: List[int], length: int) -> List[str]:
    return ['1' if occurence >= length / 2 else '0' for occurence in ones_count]


def get_least_common(ones_count: List[int], length: int) -> List[str]:
    return['0' if occurence >= length / 2 else '1' for occurence in ones_count]


def part1(most_common: List[str], least_common: List[str]) -> Tuple[int, int]:
    gamma_rate = int(''.join(most_common), 2)
    epsilon_rate = int(''.join(least_common), 2)
    return gamma_rate, epsilon_rate


def reduce_list(lines: List[str], commonnes_function) -> str:
    reduced_list = lines.copy()
    for i in range(len(lines[0])):
        occurences_of_one = get_ones_count(reduced_list)
        commonness = commonnes_function(occurences_of_one, len(reduced_list))
        reduced_list = [line for line in reduced_list if line[i] == commonness[i]]
        if len(reduced_list) == 1:
            return reduced_list[0]
    return ''


def part2(lines: List[str]) -> Tuple[int, int]:
    oxygen_generator_rating = int(''.join(reduce_list(lines, get_most_common)), 2)
    co2_scrubber_rating = int(''.join(reduce_list(lines, get_least_common)), 2)
    return oxygen_generator_rating, co2_scrubber_rating


if __name__ == '__main__':
    lines = read_input()
    occurences_of_one = get_ones_count(lines)
    most_common = get_most_common(occurences_of_one, len(lines))
    least_common = get_least_common(occurences_of_one, len(lines))
    gamma_rate, epsilon_rate = part1(most_common, least_common)
    print(gamma_rate * epsilon_rate)
    oxygen_generator_rating, co2_scrubber_rating = part2(lines)
    print(oxygen_generator_rating * co2_scrubber_rating)
