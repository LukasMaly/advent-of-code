#!/usr/bin/env python3

'''Day 2: Dive!
https://adventofcode.com/2021/day/2
'''

from typing import List, Tuple


def read_input() -> Tuple[List[str], List[int]]:
    commands = []
    units = []
    with open('inputs/day02.txt') as f:
        for line in f:
            c, u = line.split()
            commands.append(c)
            units.append(int(u))
    return commands, units


def part1(commands: List[str], units: List[int]) -> Tuple[int, int]:
    directions = {'forward': 0, 'down': 0, 'up': 0}
    for c, u in zip(commands, units):
        directions[c] += u
    horizontal = directions['forward']
    depth = directions['down'] - directions['up']
    return horizontal, depth


def part2(commands: List[str], units: List[int]) -> Tuple[int, int]:
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
    return horizontal, depth


if __name__ == '__main__':
    commands, units = read_input()
    horizontal, depth = part1(commands, units)
    print(horizontal * depth)
    horizontal, depth = part2(commands, units)
    print(horizontal * depth)
