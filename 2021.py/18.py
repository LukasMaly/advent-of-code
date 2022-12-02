#!/usr/bin/env python3

'''Day 18: Snailfish
https://adventofcode.com/2021/day/18
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        numbers = self.parse_input(lines)
        result = numbers[0]
        for number in numbers[1:]:
            result = self.add(result, number)
            result = self.reduce(result)
        return self.magnitude(result)

    def part2(self, lines: list[str]) -> int:
        from copy import deepcopy
        numbers = self.parse_input(lines)
        largest_magnitude = 0
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                for number1, number2 in zip([deepcopy(numbers[i]), deepcopy(numbers[j])], [deepcopy(numbers[j]), deepcopy(numbers[i])]):
                    result = self.add(number1, number2)
                    result = self.reduce(result)
                    magnitude = self.magnitude(result)
                    if magnitude > largest_magnitude:
                        largest_magnitude = magnitude
        return largest_magnitude

    def parse_input(self, lines: list[str]) -> list[dict[str, list[int]]]:
        import json
        numbers = []
        for line in lines:
            value = json.loads(line)
            values = []
            depths = []
            self.add_value(value, values, depths)
            numbers.append({'values': values, 'depths': depths})
        return numbers

    def add_value(self, value: list, values: list[int] = [], depths: list[int] = [], depth: int = 0):
        for i in range(2):
            if type(value[i]) == int:
                values.append(value[i])
                depths.append(depth)
            else:
                self.add_value(value[i], values, depths, depth + 1)

    def add(self, number1: dict[str, list[int]], number2: dict[str, list[int]]) -> dict[str, list[int]]:
        number1['values'].extend(number2['values'])
        number1['depths'].extend(number2['depths'])
        number1['depths'] = [depth + 1 for depth in number1['depths']]
        return number1

    def reduce(self, number: dict[str, list[int]]) -> dict[str, list[int]]:
        import math
        reduced = False
        while not reduced:
            reduced = True
            # Explode
            if any([depth >= 4 for depth in number['depths']]):
                for i, depth in enumerate(number['depths']):
                    if depth >= 4:
                        if i > 0:
                            number['values'][i - 1] += number['values'][i]
                        if i < len(number['values']) - 2:
                            number['values'][i + 2] += number['values'][i + 1]
                        del number['values'][i]
                        del number['depths'][i]
                        number['values'][i] = 0
                        number['depths'][i] -= 1
                        break
                reduced = False
            # Split
            elif any([value >= 10 for value in number['values']]):
                for i, value in enumerate(number['values']):
                    if value >= 10:
                        number['values'][i] = math.floor(value / 2)
                        number['values'].insert(i + 1, math.ceil(value / 2))
                        number['depths'][i] += 1
                        number['depths'].insert(i + 1, number['depths'][i])
                        break
                reduced = False
        return number

    def magnitude(self, number: dict[str, list[int]]) -> int:
        while not len(number['values']) == 1:
            max_depth = max(number['depths'])
            while max(number['depths']) == max_depth:
                for i, depth in enumerate(number['depths']):
                    if depth == max_depth:
                        number['values'][i] = 3 * number['values'][i] + 2 * number['values'][i + 1]
                        number['depths'][i] -= 1
                        del number['values'][i + 1]
                        del number['depths'][i + 1]
        return number['values'][0]
                    

if __name__ == '__main__':
    Puzzle().run()
