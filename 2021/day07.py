#!/usr/bin/env python3

'''Day 7: The Treachery of Whales
https://adventofcode.com/2021/day/7
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, input: list[str]) -> int:
        nums = list(map(int, input[0].split(',')))
        minimum = min(nums)
        maximum = max(nums)
        fuels = [sum([self.penalty1(num, pos) for num in nums]) for pos in range(minimum, maximum + 1)]
        return min(fuels)

    def part2(self, input: list[str]) -> int:
        nums = list(map(int, input[0].split(',')))
        minimum = min(nums)
        maximum = max(nums)
        fuels = [sum([self.penalty2(num, pos) for num in nums]) for pos in range(minimum, maximum + 1)]
        return min(fuels)

    def penalty1(self, num1: int, num2: int) -> int:
        return abs(num1 - num2)

    def penalty2(self, num1: int, num2: int) -> int:
        diff = abs(num1 - num2)
        return int(diff * (diff + 1) / 2)


if __name__ == '__main__':
    Puzzle().run()
