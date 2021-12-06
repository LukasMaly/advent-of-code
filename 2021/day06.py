#!/usr/bin/env python3

'''Day 6: Lanternfish
https://adventofcode.com/2021/day/6
'''

from utils import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self) -> None:
        super().__init__()

    def simulate_lanternfish(self, fish: list[int], days: int):
        zero_pointer = 0
        seven = 0
        eight = 0
        for i in range(days):
            zero_pointer += 1
            if zero_pointer == 7:
                zero_pointer = 0
            six_pointer = (zero_pointer + 6) % 7
            new_fish = fish[six_pointer]
            fish[six_pointer] += seven
            seven, eight = eight, new_fish
        return sum(fish + [seven, eight])

    def parse_input(self, input: list[str]) -> list[int]:
        fish = [0] * 7
        for f in map(int, input[0].split(',')):
            fish[f] += 1
        return fish

    def part1(self, input: list[str]) -> int:
        fish = self.parse_input(input)
        return self.simulate_lanternfish(fish, 80)

    def part2(self, input: list[str]) -> int:
        fish = self.parse_input(input)
        return self.simulate_lanternfish(fish, 256)


if __name__ == '__main__':
    Puzzle().run()
