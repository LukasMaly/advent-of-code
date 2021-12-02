#!/usr/bin/env python3

'''Day 1: Sonar Sweep
https://adventofcode.com/2021/day/1
'''

from typing import List


def read_input() -> List[int]:
    with open('inputs/day01.txt') as f:
        return [int(line) for line in f]


def part1(nums: List[int]) -> int:
    return sum(b > a for a, b in zip(nums, nums[1:]))


def part2(nums: List[int]) -> int:
    return sum(b > a for a, b in zip(nums, nums[3:]))


if __name__ == '__main__':
    nums = read_input()
    print(part1(nums))
    print(part2(nums))
