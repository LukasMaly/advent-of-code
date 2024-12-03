#!/usr/bin/env python3

'''Day 2: Red-Nosed Reports
https://adventofcode.com/2024/day/2
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        safe = 0
        for line in lines:
            line = line.split(' ')
            levels = list(map(int, line))
            if self.is_safe(levels):
                safe += 1
        return safe

    def part2(self, lines: list[str]) -> int:
        safe = 0
        for line in lines:
            line = line.split(' ')
            levels = list(map(int, line))
            if self.is_safe(levels):
                safe += 1
            else:
                for i in range(len(levels)):
                    tolerated_levels = levels[:i] + levels[i + 1 :]
                    if self.is_safe(tolerated_levels):
                        safe += 1
                        break
        return safe

    def is_safe(self, levels):
        diff = [a - b for a, b in zip(levels[1:], levels[:-1])]
        is_monotonic = all(i > 0 for i in diff) or all(i < 0 for i in diff)
        is_in_range = all(0 < abs(i) <= 3 for i in diff)
        if is_monotonic and is_in_range:
            return True
        return False


if __name__ == '__main__':
    Puzzle().run()
