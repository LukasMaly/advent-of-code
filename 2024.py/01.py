#!/usr/bin/env python3

'''Day 1: Historian Hysteria
https://adventofcode.com/2021/day/1
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        left, right = self.parse_input(lines)
        distance = 0
        for l, r in zip(left, right):
            distance += abs(l - r)
        return distance

    def part2(self, lines: list[str]) -> int:
        sim_score = 0
        left, right = self.parse_input(lines)
        for l in left:
            appears = 0
            if l in right:
                for r in right:
                    if l == r:
                        appears += 1
            sim_score += l * appears
        return sim_score

    def parse_input(self, lines: list[str]) -> tuple[list[int], list[int]]:
        left = []
        right = []
        for line in lines:
            l, f = line.split('   ')
            left.append(int(l))
            right.append(int(f))
        left = sorted(left)
        right = sorted(right)
        return left, right


if __name__ == '__main__':
    Puzzle().run()
