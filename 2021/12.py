#!/usr/bin/env python3

'''Day 12: Passage Pathing
https://adventofcode.com/2021/day/12
'''

from os import pardir
from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, input: list[str]) -> int:
        connections = self.parse_input(input)
        paths = []
        visited = []
        self.visit_cave('start', connections, visited[:], paths, visits=0, max_visits=1)
        return len(paths)

    def part2(self, input: list[str]) -> int:
        connections = self.parse_input(input)
        paths = []
        visited = []
        self.visit_cave('start', connections, visited[:], paths, visits=0, max_visits=2)
        return len(paths)

    def parse_input(self, input: list[str]) -> dict[str, list[str]]:
        connections = {'start': []}
        for line in input:
            caves = line.split('-')
            if 'start' in caves:
                if 'start' == caves[0]:
                    connections['start'].append(caves[1])
                else:
                    connections['start'].append(caves[0])
            elif 'end' in caves:
                if 'end' == caves[0]:
                    if caves[1] in connections:
                        connections[caves[1]].append('end')
                    else:
                        connections[caves[1]] = ['end']
                else:
                    if caves[0] in connections:
                        connections[caves[0]].append('end')
                    else:
                        connections[caves[0]] = ['end']
            else:
                if caves[0] in connections:
                    connections[caves[0]].append(caves[1])
                else:
                    connections[caves[0]] = [caves[1]]
                if caves[1] in connections:
                    connections[caves[1]].append(caves[0])
                else:
                    connections[caves[1]] = [caves[0]]
        return connections

    def visit_cave(self, target: str, connections: dict[str, list[str]], visited: list[str], paths: list[list[str]], visits: int = 0, max_visits: int = 1): 
        if self.is_small(target):
            if target in visited:
                visits += 1
                if visits == max_visits:
                    return
        visited.append(target)
        if target == 'end':
            paths.append(visited)
            return
        for cave in connections[target]:
            self.visit_cave(cave, connections, visited[:], paths, visits, max_visits)

    def is_small(self, name: str) -> bool:
        if name == 'start':
            return False
        if str.islower(name[0]):
            return True
        return False


if __name__ == '__main__':
    Puzzle().run()