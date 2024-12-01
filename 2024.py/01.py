#!/usr/bin/env python3

'''Day 1: Historian Hysteria
https://adventofcode.com/2021/day/1
'''

from collections import Counter
from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        left, right = self.parse_input(lines)
        left.sort()
        right.sort()
        return sum(abs(l - r) for l, r in zip(left, right))

    def part2(self, lines: list[str]) -> int:
        left, right = self.parse_input(lines)
        left_counter = Counter(left)
        right_counter = Counter(right)
        sim_score = 0
        for l in left_counter:
            if l in right_counter:
                sim_score += l * left_counter[l] * right_counter[l]
        return sim_score

    def parse_input(self, lines: list[str]) -> tuple[list[int], list[int]]:
        left = []
        right = []
        for line in lines:
            l, f = line.split('   ')
            left.append(int(l))
            right.append(int(f))
        return left, right


if __name__ == '__main__':
    Puzzle().run()
