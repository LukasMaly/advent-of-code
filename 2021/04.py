#!/usr/bin/env python3

'''Day 4: Giant Squid
https://adventofcode.com/2021/day/4
'''

from time import time
from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):
    
    BOARD_SIZE = 5

    def part1(self, input: list[str]) -> int:
        drawn_numbers, boards = self.parse_input(input)
        for i in range(len(drawn_numbers)):
            if i >= 4:
                for board in boards:
                    if self.is_winning(board, drawn_numbers[:i + 1]):
                        return self.board_sum(board, drawn_numbers[:i + 1]) * drawn_numbers[i]
        return 0

    def part2(self, input: list[str]) -> int:
        drawn_numbers, boards = self.parse_input(input)
        for i in range(len(drawn_numbers), -1, -1):
            for board in boards:
                if not self.is_winning(board, drawn_numbers[:i]):
                    return self.board_sum(board, drawn_numbers[:i + 1]) * drawn_numbers[i]
        return 0

    def parse_input(self, input: list[str]) -> tuple[list[int], list[list[list[int]]]]:
        drawn_numbers = list(map(int, input[0].split(',')))
        lines = input[1:]
        del lines[::6]
        lines = [list(map(int, line.split())) for line in lines]
        boards = [list(lines[(self.BOARD_SIZE * i):(self.BOARD_SIZE * i + self.BOARD_SIZE)]) for i in range(len(lines) // self.BOARD_SIZE)]
        return drawn_numbers, boards

    def has_complete_row(self, board: list[list[int]], drawn_numbers) -> bool:
        for line in board:
            if all(number in drawn_numbers for number in line):
                return True
        return False

    def transpose(self, l: list[list[int]]) -> list[list[int]]:
        return list(map(list, zip(*l)))

    def is_winning(self, board: list[list[int]], drawn_numbers: list[int]) -> bool:
        if self.has_complete_row(board, drawn_numbers):
            return True
        return self.has_complete_row(self.transpose(board), drawn_numbers)

    def board_sum(self, board: list[list[int]], drawn_numbers: list[int]) -> int:
        return sum([sum([number for number in line if number not in drawn_numbers]) for line in board])


if __name__ == '__main__':
    Puzzle().run()