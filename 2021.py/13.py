#!/usr/bin/env python3

'''Day 13: Transparent Origami
https://adventofcode.com/2021/day/13
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        dots, fold_instructions = self.parse_input(lines)
        for axis, pos in fold_instructions[:1]:
            dots = self.fold(dots, axis, pos)
        dots_count = sum([sum(row) for row in dots])
        return dots_count

    def part2(self, lines: list[str]) -> None:
        dots, fold_instructions = self.parse_input(lines)
        for axis, pos in fold_instructions:
            dots = self.fold(dots, axis, pos)
        for line in dots:
            for dot in line:
                print('#' if dot else '.', end='')
            print()
        return None

    def parse_input(self, lines: list[str]) -> tuple[list[list[int]], list[tuple[str, int]]]:
        dots_list = []
        fold_instructions = []
        for line in lines:
            if ',' in line:
                dots_list.append(list(map(int, line.split(','))))
            elif line.startswith('fold'):
                fold_instructions.append((line[11], int(line[13:])))
        cols = max(dot[0] for dot in dots_list) + 1
        rows = max(dot[1] for dot in dots_list) + 1
        dots = [[False] * cols for i in range(rows)]
        for dot in dots_list:
            dots[dot[1]][dot[0]] = True
        return dots, fold_instructions

    def flip_lr(self, x):
        return [list(reversed(row)) for row in x]

    def flip_ud(self, x):
        return list(reversed(x))

    def add(self, x, y):
        z = [[False] * len(x[0]) for i in range(len(x))]
        row_diff = len(x) - len(y)
        col_diff = len(x[0]) - len(y[0])
        for y_row in range(len(y)):
            for y_col in range(len(y[0])):
                x_row = y_row + row_diff
                x_col = y_col + col_diff
                z[x_row][x_col] = x[x_row][x_col] or y[y_row][y_col]
        return z

    def fold(self, x, axis, pos):
        if axis == 'x':
            left = [row[:pos] for row in x]
            right = [row[pos + 1:] for row in x]
            right = self.flip_lr(right)
            return self.add(left, right)
        else:  # axis == 'y'
            up = x[:pos]
            down = x[pos + 1:]
            down = self.flip_ud(down)
            return self.add(up, down)


if __name__ == '__main__':
    Puzzle().run()
