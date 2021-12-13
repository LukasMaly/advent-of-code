#!/usr/bin/env python3

'''Day 7: The Treachery of Whales
https://adventofcode.com/2021/day/7
'''

import math
import statistics

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        nums = list(map(int, lines[0].split(',')))
        median = int(statistics.median(nums))
        return sum([abs(num - median) for num in nums])

    def part2(self, lines: list[str]) -> int:
        nums = list(map(int, lines[0].split(',')))
        mean = statistics.mean(nums)
        mean_floor = math.floor(mean)
        mean_ceil = math.ceil(mean)
        fuel_mean_floor = int(sum([abs(num - mean_floor) * (abs(num - mean_floor) + 1) / 2 for num in nums]))
        fuel_mean_ceil = int(sum([abs(num - mean_ceil) * (abs(num - mean_ceil) + 1) / 2 for num in nums]))
        return min(fuel_mean_floor, fuel_mean_ceil)


if __name__ == '__main__':
    Puzzle().run()
