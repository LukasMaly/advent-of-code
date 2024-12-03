#!/usr/bin/env python3

'''Day 3: Mull It Over
https://adventofcode.com/2024/day/3
'''

import re
from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        mul_sum = 0
        pattern = r'mul\((\d+),(\d+)\)'
        line = ''.join(lines)
        matches = re.findall(pattern, line)
        for x, y in matches:
            mul_sum += int(x) * int(y)
        return mul_sum

    def part2(self, lines: list[str]) -> int:
        mul_sum = 0
        pattern1 = r"don't\(\).*?(do\(\)|$)"
        pattern2 = r'mul\((\d+),(\d+)\)'
        line = ''.join(lines)
        line = re.sub(pattern1, '', line)
        matches = re.findall(pattern2, line)
        for x, y in matches:
            mul_sum += int(x) * int(y)
        return mul_sum


if __name__ == '__main__':
    Puzzle().run()
