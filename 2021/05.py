#!/usr/bin/env python3

'''Day 5: Hydrothermal Venture
https://adventofcode.com/2021/day/5
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    DIAGRAM_SIZE = 1000

    def part1(self, lines: list[str]) -> int:
        starts, ends = self.parse_input(lines)
        diagram = [[0] * self.DIAGRAM_SIZE for i in range(self.DIAGRAM_SIZE)]
        for start, end in zip(starts, ends):
            self.draw_line(diagram, start, end, draw_diagonal=False)
        return self.count_overlaps(diagram)

    def part2(self, lines: list[str]) -> int:
        starts, ends = self.parse_input(lines)
        diagram = [[0] * self.DIAGRAM_SIZE for i in range(self.DIAGRAM_SIZE)]
        for start, end in zip(starts, ends):
            self.draw_line(diagram, start, end, draw_diagonal=True)
        return self.count_overlaps(diagram)

    def parse_input(self, lines: list[str]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        starts, ends = [], []
        for line in lines:
            start, end = line.split(' -> ')
            start = list(map(int, start.split(',')))
            end = list(map(int, end.split(',')))
            starts.append(start)
            ends.append(end)
        return starts, ends

    def draw_line(self, diagram: list[list[int]], start: tuple[int, int], end: tuple[int, int], draw_diagonal: bool = False):
        x1, y1 = start
        x2, y2 = end
        if x1 == x2:
            y1, y2 = sorted((y1, y2))
            for y in range(y1, y2 + 1):
                diagram[y][x1] += 1
        elif y1 == y2:
            x1, x2 = sorted((x1, x2))
            for x in range(x1, x2 + 1):
                diagram[y1][x] += 1
        elif draw_diagonal:
            x_step = 1
            y_step = 1
            if x2 < x1:
                x_step = -1
            if y2 < y1:
                y_step = -1
            xs = list(range(x1, x2 + x_step, x_step))
            ys = list(range(y1, y2 + y_step, y_step))
            points = zip(xs, ys)
            for x, y in points:
                diagram[y][x] += 1
    
    def count_overlaps(self, diagram: list[list[int]]) -> int:
        overlaps = 0
        for y in range(self.DIAGRAM_SIZE):
            for x in range(self.DIAGRAM_SIZE):
                if diagram[y][x] > 1:
                    overlaps += 1
        return overlaps


if __name__ == '__main__':
    Puzzle().run()
