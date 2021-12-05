#!/usr/bin/env python3

'''Day 2: Dive!
https://adventofcode.com/2021/day/2
'''

from typing import List, Tuple
from utils import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self) -> None:
        super().__init__()

    def part1(self, input: List[str]) -> int:
        commands, units = self.parse_input(input)
        directions = {'forward': 0, 'down': 0, 'up': 0}
        for c, u in zip(commands, units):
            directions[c] += u
        horizontal = directions['forward']
        depth = directions['down'] - directions['up']
        return horizontal * depth

    def part2(self, input: List[str]) -> int:
        commands, units = self.parse_input(input)
        horizontal = 0
        depth = 0
        aim = 0
        for c, u in zip(commands, units):
            if c == 'forward':
                horizontal += u
                depth += aim * u
            elif c == 'up':
                aim -= u
            elif c == 'down':
                aim += u
        return horizontal * depth

    def parse_input(self, input: List[str]) -> Tuple[List[str], List[int]]:
        commands = []
        units = []
        for line in input:
            c, u = line.split()
            commands.append(c)
            units.append(int(u))
        return commands, units


if __name__ == '__main__':
    Puzzle().run()
