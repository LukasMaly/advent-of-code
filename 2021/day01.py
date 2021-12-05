#!/usr/bin/env python3

'''Day 1: Sonar Sweep
https://adventofcode.com/2021/day/1
'''

from typing import List
from utils import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self) -> None:
        super().__init__()

    def part1(self, input: List[str]) -> int:
        nums = list(map(int, input))
        return sum(b > a for a, b in zip(nums, nums[1:]))

    def part2(self, input: List[str]) -> int:
        nums = list(map(int, input))
        return sum(b > a for a, b in zip(nums, nums[3:]))


if __name__ == '__main__':
    Puzzle().run()
