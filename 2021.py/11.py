#!/usr/bin/env python3

'''Day 11: Dumbo Octopus
https://adventofcode.com/2021/day/11
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    ADJACENTS = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

    def part1(self, lines: list[str], steps=100) -> int:
        flashes = 0
        energies = self.parse_input(lines)
        for step in range(steps):
            flashes += self.perform_step(energies)
        return flashes

    def part2(self, lines: list[str]) -> int:
        energies = self.parse_input(lines)
        steps = 0
        while True:
            steps += 1
            if self.perform_step(energies) == len(energies[0]) * len(energies):
                return steps

    def parse_input(self, lines: list[str]) -> list[list[int]]:
        energies = []
        for line in lines:
            energies.append(list(map(int, [x for x in line])))
        return energies

    def perform_step(self, energies: list[list[int]]) -> int:
        for y, row in enumerate(energies):
            for x, value in enumerate(row):
                energies[y][x] += 1
        flashed = [[False] * len(energies[0]) for i in range(len(energies))]
        for y, row in enumerate(energies):
            for x, value in enumerate(row):
                if value > 9 and not flashed[y][x]:
                    self.flash(x, y, energies, flashed)
        for y, row in enumerate(energies):
            for x, value in enumerate(row):
                if value > 9:
                    energies[y][x] = 0
        flashes = 0
        for y, row in enumerate(flashed):
            for x, value in enumerate(row):
                if value == True:
                    flashes += 1
        return flashes
    
    def flash(self, x, y, energies, flashed):
        flashed[y][x] = True
        for adjacent in self.ADJACENTS:
            dx, dy = x + adjacent[0], y + adjacent[1]
            if 0 <= dx < len(energies[0]) and 0 <= dy < len(energies):
                energies[dy][dx] += 1
                if energies[dy][dx] > 9 and not flashed[dy][dx]:
                    self.flash(dx, dy, energies, flashed)


if __name__ == '__main__':
    Puzzle().run()
