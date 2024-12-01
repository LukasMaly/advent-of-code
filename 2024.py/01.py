#!/usr/bin/env python3

'''Day 1: Historian Hysteria
https://adventofcode.com/2021/day/1
'''

from collections import Counter
from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        left, right = self.parse_input(lines)
        left = sorted(left)
        right = sorted(right)
        distances = map(lambda l, r: abs(l - r), left, right)
        distance = sum(distances)
        return distance

    def part2(self, lines: list[str]) -> int:
        left, right = self.parse_input(lines)
        sim_score = 0
        left = Counter(left)
        right = Counter(right)
        for l in left:
            if l in right:
                sim_score += l * left[l] * right[l]
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
