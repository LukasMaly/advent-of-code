#!/usr/bin/env python3

'''Day 17: Trick Shot
https://adventofcode.com/2021/day/17
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        _, ylim = self.parse_input(lines)
        return self.get_triangular(-ylim[0] - 1)

    def part2(self, lines: list[str]) -> int:
        xlim, ylim = self.parse_input(lines)
        _, ylim = self.parse_input(lines)
        area = (xlim[1] - xlim[0] + 1) * (ylim[1] - ylim[0] + 1)
        min_dx = 0
        max_dx = 0
        max_steps = 2 * (-ylim[0]) + 1
        for n in range(xlim[0]):
            if self.get_triangular(n) >= xlim[0]:
                min_dx = n
                break
        for n in range(xlim[0], 0, -1):
            if n + (n - 1) <= xlim[1]:
                max_dx = n
                break
        hits = 0
        for dy in range(ylim[1] + 1, -ylim[0]):
            for dx in range(min_dx, max_dx + 1):
                trajectory = self.get_trajectory(dx, dy, max_steps)
                for x, y in trajectory:
                    if xlim[0] <= x <= xlim[1] and ylim[0] <= y <= ylim[1]:
                        hits += 1
                        break
        return hits + area

    def parse_input(self, lines: list[str]) -> tuple[tuple[int, int], tuple[int, int]]:
        import re
        p = re.compile(r'target area: x=(-?\w+)\.\.(-?\w+), y=(-?\w+)\.\.(-?\w+)')
        m = p.match(lines[0])
        xlims = (int(m.group(1)), int(m.group(2)))
        ylims = (int(m.group(3)), int(m.group(4)))
        return xlims, ylims

    def sign(self, x: int) -> int:
        return 1 if x > 0 else (-1 if x < 0 else 0)

    def get_trajectory(self, dx, dy, steps):
        x, y = 0, 0
        result = [[x, y]]
        for t in range(1, steps):
            x += dx
            y += dy
            dx = dx - self.sign(dx)
            dy = dy - 1
            result.append([x, y])
        return result

    def get_triangular(self, n: int) -> int:
        return int((n * (n + 1)) / 2)

    # def is_square(self, x: int) -> bool:
    #     import math
    #     return x == math.isqrt(x) ** 2

    # def is_triangular(self, x: int) -> bool:
    #     return self.is_square(8 * x + 1)

    # def get_triangular_root(self, x: int) -> int:
    #     import math
    #     return int((math.sqrt(8 * x + 1) - 1) / 2)

if __name__ == '__main__':
    Puzzle().run()
