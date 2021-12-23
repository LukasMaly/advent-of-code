#!/usr/bin/env python3

'''Day 22: Reactor Reboot
https://adventofcode.com/2021/day/22
'''

import re

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        steps = self.parse_input(lines)
        on = set()
        for step in steps:
            if abs(step['x'][0]) > 50:
                return len(on)
            for x in range(step['x'][0], step['x'][1] + 1):
                for y in range(step['y'][0], step['y'][1] + 1):
                    for z in range(step['z'][0], step['z'][1] + 1):
                        if step['state']:
                            on.add((x, y, z))
                        elif (x, y, z) in on:
                            on.remove((x, y, z))
        return 0

    def part2(self, lines: list[str]) -> int:
        steps = self.parse_input(lines)
        on_cubes = set()
        for step in steps:
            on_cubes_copy = on_cubes.copy()
            new_cube = ((step['x'][0], step['x'][1]), (step['y'][0], step['y'][1]), (step['z'][0], step['z'][1]))
            if step['state']:
                intersected = False
                for on_cube in on_cubes_copy:
                    if self.have_intersection(on_cube, new_cube):
                        on_cubes.remove(on_cube)
                        sub_cubes = self.divide_cube(on_cube, new_cube)
                        on_cubes.update(sub_cubes)
                        on_cubes.add(new_cube)
                        intersected = True
                if not intersected:
                    on_cubes.add(new_cube)
            else:
                for on_cube in on_cubes_copy:
                    if self.have_intersection(on_cube, new_cube):
                        on_cubes.remove(on_cube)
                        sub_cubes = self.divide_cube(on_cube, new_cube)
                        on_cubes.update(sub_cubes)
        return self.get_volume(on_cubes)
    
    def have_intersection(self, a, b):
        for axis in range(3):
            if not ((a[axis][0] <= b[axis][0] and b[axis][0] <= a[axis][1]) or \
                (b[axis][0] <= a[axis][0] and a[axis][0] <= b[axis][1])):
                return False
        return True

    def divide_cube(self, a, b):
        sub_cubes = set()
        if b[0][0] >= a[0][0]:
            if b[0][0] != a[0][0]:
                sub_cubes.add(((a[0][0], b[0][0] - 1), a[1], a[2]))
            a = ((b[0][0], a[0][1]), a[1], a[2])
        if b[0][1] <= a[0][1]:
            if a[0][1] != b[0][1]:
                sub_cubes.add(((b[0][1] + 1, a[0][1]), a[1], a[2]))
            a = ((a[0][0], b[0][1]), a[1], a[2])
        if b[1][0] >= a[1][0]:
            if b[1][0] != a[1][0]:
                sub_cubes.add((a[0], (a[1][0], b[1][0] - 1), a[2]))
            a = (a[0], (b[1][0], a[1][1]), a[2])
        if b[1][1] <= a[1][1]:
            if a[1][1] != b[1][1]:
                sub_cubes.add((a[0], (b[1][1] + 1, a[1][1]), a[2]))
            a = (a[0], (a[1][0], b[1][1]), a[2])
        if b[2][0] >= a[2][0]:
            if b[2][0] != a[2][0]:
                sub_cubes.add((a[0], a[1], (a[2][0], b[2][0] - 1)))
            a = (a[0], a[1], (b[2][0], a[2][1]))
        if b[2][1] <= a[2][1]:
            if a[2][1] != b[2][1]:
                sub_cubes.add((a[0], a[1], (b[2][1] + 1, a[2][1])))
            a = (a[0], a[1], (a[2][0], b[2][1]))
        return sub_cubes

    def get_volume(self, cubes):
        volume = 0
        for cube in cubes:
            volume += (cube[0][1] - cube[0][0] + 1) * (cube[1][1] - cube[1][0] + 1) * (cube[2][1] - cube[2][0] + 1)
        return volume

    def parse_input(self, lines: list[str]) -> list[dict]:
        steps = []
        p = re.compile(r'(\D+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)')
        for line in lines:
            m = p.match(line)
            steps.append({'state': True if m.group(1) == 'on' else False, 'x': (int(m.group(2)), int(m.group(3))), 'y': (int(m.group(4)), int(m.group(5))), 'z': (int(m.group(6)), int(m.group(7)))})
        return steps

if __name__ == '__main__':
    Puzzle().run()
