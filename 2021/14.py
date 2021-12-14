#!/usr/bin/env python3

'''Day 14: Extended Polymerization
https://adventofcode.com/2021/day/14
'''

from os import pardir
from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        polymer, pair_insertions = self.parse_input(lines)
        pair_count = self.get_pair_count(polymer, pair_insertions, steps=10)
        element_occurences = self.count_element_occurences(pair_count, polymer[0])
        element_occurences = dict(sorted(element_occurences.items(), key=lambda item: item[1]))
        return list(element_occurences.values())[-1] - list(element_occurences.values())[0]

    def part2(self, lines: list[str]) -> int:
        polymer, pair_insertions = self.parse_input(lines)
        pair_count = self.get_pair_count(polymer, pair_insertions, steps=40)
        element_occurences = self.count_element_occurences(pair_count, polymer[0])
        element_occurences = dict(sorted(element_occurences.items(), key=lambda item: item[1]))
        return list(element_occurences.values())[-1] - list(element_occurences.values())[0]

    def get_pair_count(self, polymer: str, pair_insertions: dict[str, str], steps: int = 1) -> dict[str, int]:
        pair_children = {key: (key[0] + value, value + key[1]) for key, value in pair_insertions.items()}
        pair_count = {key: 0 for key in pair_insertions}
        for i, j in zip(polymer[:-1], polymer[1:]):
            pair_count[i + j] += 1
        for i in range(steps):
            new_pair_count = {key: 0 for key in pair_insertions}
            for pair, count in pair_count.items():
                new_pair_count[pair_children[pair][0]] += count
                new_pair_count[pair_children[pair][1]] += count
            pair_count = new_pair_count
        return pair_count
    
    def count_element_occurences(self, pair_count: dict[str, int], first_element: str) -> dict[str, int]:
        elements = list(set(''.join(pair_count.keys())))
        element_occurences = {key: 0 for key in elements}
        element_occurences[first_element] = 1
        for pair, count in pair_count.items():
            element_occurences[pair[1]] += count
        return element_occurences

    def parse_input(self, lines: list[str]) -> tuple[str, dict[str, str]]:
        polymer_template = lines[0]
        pair_insertions = {}
        for line in lines[2:]:
            left, right = line.split(' -> ')
            pair_insertions[left] = right
        return polymer_template, pair_insertions


if __name__ == '__main__':
    Puzzle().run()
