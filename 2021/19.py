#!/usr/bin/env python3

'''Day 19: Beacon Scanner
https://adventofcode.com/2021/day/19
'''

import math

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        scanners = self.parse_input(lines)
        beacons_set = self.get_beacons_set(scanners)
        return len(beacons_set)

    def part2(self, lines: list[str]) -> int:
        scanners = self.parse_input(lines)
        scanner_positions = self.get_scanner_positions(scanners)
        distances = [[self.get_manhattan_distance(point1, point2) for point2 in scanner_positions] for point1 in scanner_positions]
        return max([max(row) for row in distances])

    def parse_input(self, lines: list[str]) -> list[list[list[int]]]:
        scanners = []
        scanner = []
        for line in lines:
            if line.startswith('---'):
                scanner = []
            elif len(line) == 0:
                scanners.append(scanner)
            else:
                scanner.append(list(map(int, line.split(','))))
        scanners.append(scanner)
        return scanners

    def get_beacons_set(self, scanners):
        beacons_distances = self.get_beacons_distances(scanners)
        common_beacons = self.get_common_beacons(beacons_distances)
        tree = self.get_tree(list(common_beacons), 0)
        pairs = self.get_pairs(tree)
        scanners_transforms, scanners_translations = self.get_scanners_transforms(pairs, common_beacons, scanners)
        transformed_beacons = self.transform_beacons(scanners, tree, scanners_transforms, scanners_translations, 0, self.ROTATION_MATRICES[0], [[0, 0, 0]])
        return set(tuple(beacon) for beacon in transformed_beacons)

    def get_scanner_positions(self, scanners):
        beacons_distances = self.get_beacons_distances(scanners)
        common_beacons = self.get_common_beacons(beacons_distances)
        tree = self.get_tree(list(common_beacons), 0)
        pairs = self.get_pairs(tree)
        scanners_transforms, scanners_translations = self.get_scanners_transforms(pairs, common_beacons, scanners)
        return self.transform_scanners(scanners, tree, scanners_transforms, scanners_translations, 0, self.ROTATION_MATRICES[0], [[0, 0, 0]])

    def get_beacons_distances(self, scanners):
        beacons_distances = []
        for scanner in scanners:
            beacons = []
            for i in range(len(scanner)):
                distances = []
                for j in range(len(scanner)):
                    distances.append(self.get_euclidean_distance(scanner[i], scanner[j]))
                beacons.append(distances)
            beacons_distances.append(beacons)
        return beacons_distances

    def get_common_beacons(self, beacon_distances):
        common_beacons = {}
        for i in range(len(beacon_distances) - 1):
            for j in range(i + 1, len(beacon_distances)):
                for m in range(len(beacon_distances[i])):
                    common_distances = []
                    for n in range(len(beacon_distances[j])):
                        common_distances.append(self.get_common_elements(beacon_distances[i][m], beacon_distances[j][n]))
                    for n in range(len(common_distances)):
                        if common_distances[n] >= 11:
                            if (i, j) in common_beacons:
                                common_beacons[(i, j)].append((m, n))
                            else:
                                common_beacons[(i, j)] = [(m, n)]
        return common_beacons

    def get_transformations(self, beacon1, beacon2):
        for rotation_matrix in self.ROTATION_MATRICES:
            transformed_points2 = self.matmul(beacon2, rotation_matrix)
            distances = []
            for point1, point2 in zip(beacon1[:3], transformed_points2[:3]):
                distances.append(self.get_euclidean_distance(point1, point2))
            if distances[0] == distances[1] == distances[2]:
                transformed_points2 = [[int(round(x)) for x in points] for points in transformed_points2]
                scanners_transforms = rotation_matrix
                scanners_translations = [beacon1[0][i] - transformed_points2[0][i] for i in range(3)]
                return scanners_transforms, scanners_translations

    def transform_beacons(self, scanners, tree, transforms, translations, parent, transformation, translation, transformed_beacons=[], scanner_positions=[]):
        beacons = scanners[parent]
        beacons = self.matmul(beacons, transformation, int)
        beacons = [[x + tx, y + ty, z + tz] for (x, y, z), (tx, ty, tz) in zip(beacons, translation * len(beacons))]
        transformed_beacons.extend(beacons)
        for child in tree[parent]:
            pair = (parent, child)
            child_transformation = transforms[pair]
            child_translation = translations[pair]
            child_translation = self.matmul([child_translation], transformation, int)
            child_translation = [[x + y for x, y in zip(translation[0], child_translation[0])]]
            child_transformation = self.matmul(child_transformation, transformation)
            transformed_beacons = self.transform_beacons(scanners, tree, transforms, translations, child, child_transformation, child_translation, transformed_beacons)
        return transformed_beacons

    def transform_scanners(self, scanners, tree, transforms, translations, parent, transformation, translation, scanner_positions=[]):
        scanner_positions.extend(translation)
        for child in tree[parent]:
            pair = (parent, child)
            child_transformation = transforms[pair]
            child_translation = translations[pair]
            child_translation = self.matmul([child_translation], transformation, int)
            child_translation = [[x + y for x, y in zip(translation[0], child_translation[0])]]
            child_transformation = self.matmul(child_transformation, transformation)
            scanner_positions = self.transform_scanners(scanners, tree, transforms, translations, child, child_transformation, child_translation, scanner_positions)
        return scanner_positions

    def get_scanners_transforms(self, pairs, common_beacons, scanners):
        scanners_transforms = {}
        scanners_translations = {}
        for parent, child in pairs:
            for pair in common_beacons:
                if parent in pair and child in pair:
                    beacon1 = []
                    beacon2 = []
                    for i in range(len(common_beacons[pair])):
                        beacon1.append(scanners[pair[0]][common_beacons[pair][i][0]])
                        beacon2.append(scanners[pair[1]][common_beacons[pair][i][1]])
                    if child == pair[0]:
                        beacon1, beacon2 = beacon2, beacon1
                    scanners_transforms[(parent, child)], scanners_translations[(parent, child)] = self.get_transformations(beacon1, beacon2)
        return scanners_transforms, scanners_translations

    def get_tree(self, edges, root):
        tree = {root: []}
        children = []
        for edge in edges:
            if root in edge:
                if edge[1] == root:
                    edge = edge[::-1]
                tree[edge[0]].append(edge[1])
            else:
                children.append(edge)
        for i in tree[root]:
            tree.update(self.get_tree(children, i))
        return tree

    def get_pairs(self, tree):
        pairs = []
        for parent in tree:
            for child in tree[parent]:
                pairs.append((parent, child))
        return pairs
        
    def matmul(self, x, y, dtype=float):
        result = [[sum(a*b for a, b in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]
        if dtype == int:
            result = [[int(round(x)) for x in row] for row in result]
        return result
    
    def get_euclidean_distance(self, point1: list[int], point2: list[int]) -> int:
        return int(math.sqrt(math.pow(point2[0] - point1[0], 2) + math.pow(point2[1] - point1[1], 2) + math.pow(point2[2] - point1[2], 2)))

    def get_manhattan_distance(self, point1: list[int], point2: list[int]) -> int:
        return int(abs(point2[0] - point1[0]) + abs(point2[1] - point1[1]) + abs(point2[2] - point1[2]))

    def get_common_elements(self, distances1, distances2):
        common_elements = 0
        for i in range(len(distances1)):
            for j in range(len(distances2)):
                if distances1[i] == distances2[j]:
                    common_elements += 1
        return common_elements - 1

    ROTATION_MATRICES = [[[  1,  0,  0],
                          [  0,  1,  0],
                          [  0,  0,  1]],

                         [[  1,  0,  0],
                          [  0,  0, -1],
                          [  0,  1,  0]],

                         [[  1,  0,  0],
                          [  0, -1,  0],
                          [  0,  0, -1]],

                         [[  1,  0,  0],
                          [  0,  0,  1],
                          [  0, -1,  0]],

                         [[  0, -1,  0],
                          [  1,  0,  0],
                          [  0,  0,  1]],

                         [[  0,  0,  1],
                          [  1,  0,  0],
                          [  0,  1,  0]],

                         [[  0,  1,  0],
                          [  1,  0,  0],
                          [  0,  0, -1]],

                         [[  0,  0, -1],
                          [  1,  0,  0],
                          [  0, -1,  0]],

                         [[ -1,  0,  0],
                          [  0, -1,  0],
                          [  0,  0,  1]],

                         [[- 1,  0,  0],
                          [  0,  0, -1],
                          [  0, -1,  0]],

                         [[ -1,  0,  0],
                          [  0,  1,  0],
                          [  0,  0, -1]],

                         [[ -1,  0,  0],
                          [  0,  0,  1],
                          [  0,  1,  0]],

                         [[  0,  1,  0],
                          [ -1,  0,  0],
                          [  0,  0,  1]],

                         [[  0,  0,  1],
                          [ -1,  0,  0],
                          [  0, -1,  0]],

                         [[  0, -1,  0],
                          [ -1,  0,  0],
                          [  0,  0, -1]],

                         [[  0,  0, -1],
                          [ -1,  0,  0],
                          [  0,  1,  0]],

                         [[  0,  0, -1],
                          [  0,  1,  0],
                          [  1,  0,  0]],

                         [[  0,  1,  0],
                          [  0,  0,  1],
                          [  1,  0,  0]],

                         [[  0,  0,  1],
                          [  0, -1,  0],
                          [  1,  0,  0]],

                         [[  0, -1,  0],
                          [  0,  0, -1],
                          [  1,  0,  0]],

                         [[  0,  0, -1],
                          [  0, -1,  0],
                          [ -1,  0,  0]],

                         [[  0, -1,  0],
                          [  0,  0,  1],
                          [ -1,  0,  0]],

                         [[  0,  0,  1],
                          [  0,  1,  0],
                          [ -1,  0,  0]],

                         [[  0,  1,  0],
                          [  0,  0, -1],
                          [ -1,  0,  0]]]


if __name__ == '__main__':
    Puzzle().run()
