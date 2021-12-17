#!/usr/bin/env python3

'''Day 15: Chiton
https://adventofcode.com/2021/day/15
'''

import sys
from typing import List
from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        risk_levels = self.parse_input(lines)
        return self.dijkstra(risk_levels)

    def part2(self, lines: list[str]) -> int:
        risk_levels = self.parse_input(lines)
        height, width = len(risk_levels), len(risk_levels[0])
        full_risk_levels = [[(risk_levels[j % width][i % height] + (i // width) + (j // height)) for i in range(5 * width)] for j in range(5 * height)]
        full_risk_levels = [[value if value < 10 else value % 9 for value in row] for row in full_risk_levels]
        return self.dijkstra(full_risk_levels)

    def parse_input(self, lines: list[str]) -> list[list[int]]:
        risk_levels = []
        for line in lines:
            risk_levels.append(list(map(int, [x for x in line])))
        return risk_levels

    def dijkstra(self, a: list[list[int]]) -> int:
        height, width = len(a), len(a[0])
        dist = [[sys.maxsize] * width for i in range(height)]
        dist[0][0] = 0
        prev = [[[0, 0]] * width for i in range(height)]
        visited = [[False] * width for i in range(height)]
        x, y = 0, 0
        while True:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= y + dy < height and 0 <= x + dx < width:
                    if not visited[y + dy][x + dx] and dist[y + dy][x + dx] > a[y + dy][x + dx] + dist[y][x]:
                        dist[y + dy][x + dx] = a[y + dy][x + dx] + dist[y][x]
                        prev[y + dy][x + dx] = [y, x]
            visited[y][x] = True
            dist[y][x] = sys.maxsize
            row_mins = [min(row) for row in dist]
            min_dist = min(row_mins)
            y = row_mins.index(min_dist)
            x = dist[y].index(min_dist)
            if y == height - 1 and x == width - 1:
                break
        # path = []
        # y, x = height - 1, width - 1
        # while y > 0 or x > 0:
        #     path.append([y, x])
        #     y, x = prev[y][x]
        # path.append([y, x])
        return dist[height - 1][width - 1]


if __name__ == '__main__':
    Puzzle().run()
