#!/usr/bin/env python3

'''Day 4: Giant Squid
https://adventofcode.com/2021/day/4
'''

import copy
from typing import List, Tuple


BOARD_SIZE = 5


def read_input() -> Tuple[List[int], List[List[List[int]]]]:
    with open('inputs/day04.txt') as f:
        drawn_numbers = list(map(int, f.readline().split(',')))
        lines = f.readlines()
        del lines[::6]
        lines = [list(map(int, line.split())) for line in lines]
        boards = [list(lines[(BOARD_SIZE * i):(BOARD_SIZE * i + BOARD_SIZE)]) for i in range(len(lines) // BOARD_SIZE)]
        return drawn_numbers, boards


def has_complete_row(board: List[List[int]]):
    for line in board:
        if sum([x is None for x in line]) == BOARD_SIZE:
            return True
    return False


def transpose(l: List[List[int]]) -> List[List[int]]:
    return list(map(list, zip(*l)))


def is_winning(board: List[List[int]]) -> bool:
    if has_complete_row(board):
        return True
    board = transpose(board)
    if has_complete_row(board):
        return True
    return False


def board_sum(board: List[List[int]]) -> int:
    return sum([sum(filter(None, line)) for line in board])


def remove_drawn_number(drawn_number: int, boards: List[List[List[int]]]) -> List[List[List[int]]]:
    for b, board in enumerate(boards):
        for y, line in enumerate(board):
            for x, number in enumerate(line):
                if number == drawn_number:
                    boards[b][y][x] = None
    return boards
    

def part1(drawn_numbers: List[int], boards: List[List[List[int]]]) -> int:
    for drawn_number in drawn_numbers:
        boards = remove_drawn_number(drawn_number, boards)
        for board in boards:
            if is_winning(board):
                return board_sum(board) * drawn_number
    return 0


def part2(drawn_numbers: List[int], boards: List[List[List[int]]]) -> int:
    for drawn_number in drawn_numbers:
        boards = remove_drawn_number(drawn_number, boards)
        if len(boards) == 1:
            if is_winning(boards[0]):
                return board_sum(boards[0]) * drawn_number
        else:
            boards = [board for board in boards if not is_winning(board)]
    return 0


if __name__ == '__main__':
    drawn_numbers, boards = read_input()
    score = part1(drawn_numbers, copy.deepcopy(boards))
    print(score)
    score = part2(drawn_numbers, copy.deepcopy(boards))
    print(score)
