#!/usr/bin/env python3

'''Day 4: Giant Squid
https://adventofcode.com/2021/day/4
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):
    
    BOARD_SIZE = 5

    def part1(self, input: list[str]) -> int:
        drawn_numbers, boards = self.parse_input(input)
        for drawn_number in drawn_numbers:
            boards = self.remove_drawn_number(drawn_number, boards)
            for board in boards:
                if self.is_winning(board):
                    return self.board_sum(board) * drawn_number
        return 0

    def part2(self, input: list[str]) -> int:
        drawn_numbers, boards = self.parse_input(input)
        for drawn_number in drawn_numbers:
            boards = self.remove_drawn_number(drawn_number, boards)
            if len(boards) == 1:
                if self.is_winning(boards[0]):
                    return self.board_sum(boards[0]) * drawn_number
            else:
                boards = [board for board in boards if not self.is_winning(board)]
        return 0

    def parse_input(self, input: list[str]) -> tuple[list[int], list[list[list[int]]]]:
        drawn_numbers = list(map(int, input[0].split(',')))
        lines = input[1:]
        del lines[::6]
        lines = [list(map(int, line.split())) for line in lines]
        boards = [list(lines[(self.BOARD_SIZE * i):(self.BOARD_SIZE * i + self.BOARD_SIZE)]) for i in range(len(lines) // self.BOARD_SIZE)]
        return drawn_numbers, boards

    def has_complete_row(self, board: list[list[int | None]]) -> bool:
        for line in board:
            if sum([x is None for x in line]) == self.BOARD_SIZE:
                return True
        return False

    def transpose(self, l: list[list[int | None]]) -> list[list[int | None]]:
        return list(map(list, zip(*l)))

    def is_winning(self, board: list[list[int | None]]) -> bool:
        if self.has_complete_row(board):
            return True
        board = self.transpose(board)
        if self.has_complete_row(board):
            return True
        return False

    def board_sum(self, board: list[list[int | None]]) -> int:
        return sum([sum(filter(None, line)) for line in board])

    def remove_drawn_number(self, drawn_number: int, boards: list[list[list[int | None]]]) -> list[list[list[int | None]]]:
        for b, board in enumerate(boards):
            for y, line in enumerate(board):
                for x, number in enumerate(line):
                    if number == drawn_number:
                        boards[b][y][x] = None
        return boards                   


if __name__ == '__main__':
    Puzzle().run()
