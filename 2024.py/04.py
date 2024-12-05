#!/usr/bin/env python3

'''Day 4: Ceres Search
https://adventofcode.com/2024/day/4
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        border = 3
        word_search = self.parse_input(lines, border)
        height = len(word_search) - 2 * border
        width = len(word_search[0]) - 2 * border
        n_xmas = 0
        for i in range(border, height + border):
            for j in range(border, width + border):
                if word_search[i][j] == 'X':
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if word_search[i + 1 * x][j + 1 * y] == 'M':
                                if word_search[i + 2 * x][j + 2 * y] == 'A':
                                    if word_search[i + 3 * x][j + 3 * y] == 'S':
                                        n_xmas += 1
        return n_xmas

    def part2(self, lines: list[str]) -> int:
        border = 1
        word_search = self.parse_input(lines, border)
        height = len(word_search) - 2 * border
        width = len(word_search[0]) - 2 * border
        n_xmas = 0
        for i in range(border, height + border):
            for j in range(border, width + border):
                if word_search[i][j] == 'A':
                    n_mas = 0
                    for x in [-1, 1]:
                        for y in [-1, 1]:
                            if word_search[i + x][j + y] == 'M':
                                if word_search[i - x][j - y] == 'S':
                                    n_mas += 1
                    if n_mas == 2:
                        n_xmas += 1
        return n_xmas

    def parse_input(self, lines: list[str], border=0) -> list[list[str]]:
        words_search = []
        for i in range(border):
            words_search.append('.' * (len(lines[0]) + 2 * border))
        for line in lines:
            words_search.append('.' * border + line + '.' * border)
        for i in range(border):
            words_search.append('.' * (len(lines[0]) + 2 * border))
        return words_search


if __name__ == '__main__':
    Puzzle().run()
