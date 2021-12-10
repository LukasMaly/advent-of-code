#!/usr/bin/env python3

'''Day 9: Smoke Basin
https://adventofcode.com/2021/day/9
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, input: list[str]) -> int:
        directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        heightmap = self.parse_input(input)
        height = len(heightmap)
        width = len(heightmap[0])
        heightmap = self.add_padding(heightmap)
        low_points = []
        for y in range(1, height + 1):
            for x in range(1, width + 1):
                adjacent = sorted([heightmap[y + directions[direction][0]][x + directions[direction][1]] for direction in directions])
                if heightmap[y][x] < adjacent[0]:
                    low_points.append(heightmap[y][x])
        for i in range(len(low_points)):
            low_points[i] += 1
        return sum(low_points)

    def part2(self, input: list[str]) -> int:
        heightmap = self.parse_input(input)
        labels = self.connected_component_labeling(heightmap)
        basins = {}
        for y, row in enumerate(labels):
            for x, label in enumerate(row):
                if label > 0:
                    if label in basins:
                        basins[label] += 1
                    else:
                        basins[label] = 1
        largest_basins = sorted(basins.values())[-3:]
        result = 1
        for x in largest_basins:
            result *= x
        return result

    def parse_input(self, input: list[str]) -> list[list[int]]:
        heightmap = []
        for line in input:
            heightmap.append(list(map(int, [x for x in line])))
        return heightmap

    def add_padding(self, heightmap: list[list[int]], value: int = 9):
        for i in range(len(heightmap)):
            heightmap[i] = [value] + heightmap[i] + [value]
        heightmap.insert(0, [value] * len(heightmap[0]))
        heightmap.append([value] * len(heightmap[0]))
        return heightmap

    def connected_component_labeling(self, heightmap: list[list[int]]) -> list[list[int]]:
        """Two pass algorithm"""
        linked = []
        labels = [[0] * len(heightmap[0]) for i in range(len(heightmap))]
        next_label = 0
        # First pass
        for y, row in enumerate(heightmap):
            for x, value in enumerate(row):
                if value < 9:
                    neighbours = []
                    if x > 0:
                        if labels[y][x - 1] > 0:
                            neighbours.append(labels[y][x - 1])
                    if y > 0:
                        if labels[y - 1][x] > 0:
                            neighbours.append(labels[y - 1][x])
                    if len(neighbours) == 0:
                        next_label += 1
                        labels[y][x] = next_label
                    elif len(neighbours) == 1:
                        labels[y][x] = neighbours[0]
                    else:  # len(neighbours) == 2:
                        neighbours = set(neighbours)
                        if len(neighbours) == 1:
                            labels[y][x] = min(neighbours)
                        else:  # len(neighbours) == 2
                            label = min(neighbours)
                            for i in range(len(linked)):
                                if label in linked[i]:
                                    linked[i] = linked[i].union(neighbours)
                                    break
                            else:
                                linked.append(neighbours)
                            labels[y][x] = label
        final_labels = {}
        new_label_number = 1
        # Second pass
        for y, row in enumerate(labels):
            for x, value in enumerate(row):
                if value > 0:
                    new_label = value
                    for i in range(len(linked)):
                        if value in linked[i]:
                            new_label = min(linked[i])
                            labels[y][x] = new_label
                            break
                    if new_label not in final_labels:
                        final_labels[new_label] = new_label_number
                        new_label_number = new_label_number + 1
        # Third pass
        for y, row in enumerate(labels):
            for x, value in enumerate(row):
                if value > 0:           
                    labels[y][x] = final_labels[value]
        return labels


if __name__ == '__main__':
    Puzzle().run()
