#!/usr/bin/env python3

'''Day 8: Seven Segment Search
https://adventofcode.com/2021/day/8
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, input: list[str]) -> int:
        DIGIT_LENS = [2, 4, 3, 7]  # 1, 4, 7, 8
        result = 0
        _, values = self.parse_input(input)
        for value in values:
            for digit in value:
                if len(digit) in DIGIT_LENS:
                    result += 1
        return result

    def part2(self, input: list[str]) -> int:
        results = []
        patterns, values = self.parse_input(input)
        for pattern, value in zip(patterns, values):
            pattern_mapping = self.decode_pattern(pattern)
            keys = [self.sorted_str([char for char in digit]) for digit in value]
            results.append(int(''.join([pattern_mapping[key] for key in keys])))
        return(sum(results))

    def parse_input(self, input: list[str]) -> tuple[list[str], list[str]]:
        patterns = []
        values = []
        for line in input:
            pattern, value = line.split(' | ')
            pattern = pattern.split()
            value = value.split()
            patterns.append(pattern)
            values.append(value)
        return patterns, values

    def sorted_str(self, string):
        return ''.join(sorted(string))

    def intersection(self, string1, string2):
        return self.sorted_str(set([char for char in string1]).intersection(set([char for char in string2])))

    def difference(self, string1, string2):
        return self.sorted_str(set([char for char in string1]).difference(set([char for char in string2])))

    def decode_pattern(self, pattern):
        DIGIT_LENS = {'2': '1', '4': '4', '3': '7', '7': '8'}
        segments_mapping = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': ''}
        digits = {'0': '', '1': '', '2': '', '3': '', '4': '',
                  '5': '', '6': '', '7': '', '8': '', '9': ''}
        pattern = [self.sorted_str(digit) for digit in pattern]
        for digit in pattern:
            if str(len(digit)) in DIGIT_LENS:
                digits[DIGIT_LENS[str(len(digit))]] = digit
        for char in digits['7']:
            if char not in digits['1']:
                segments_mapping['a'] = char
                break
        len_5 = [digit for digit in pattern if len(digit) == 5]
        len_6 = [digit for digit in pattern if len(digit) == 6]
        horizontal = self.intersection(self.intersection(len_5[0], len_5[1]), len_5[2])
        right_vertical = digits['1']
        for digit in len_5:
            if len(self.intersection(digits['1'], digit)) == 2:
                digits['3'] = digit
        left_vertical = self.difference(digits['8'], digits['3'])
        for digit in len_6:
            difference = self.difference(digits['8'], digit)
            if difference in horizontal:
                digits['0'] = self.sorted_str(digit)
                segments_mapping['d'] = difference
            elif difference in left_vertical:
                digits['9'] = self.sorted_str(digit)
                segments_mapping['e'] = difference
            elif difference in right_vertical:
                digits['6'] = self.sorted_str(digit)
                segments_mapping['c'] = difference
        for char in right_vertical:
            if char != segments_mapping['c']:
                segments_mapping['f'] = char
        for char in left_vertical:
            if char != segments_mapping['e']:
                segments_mapping['b'] = char
        for digit in len_5:
            if segments_mapping['c'] not in digit:
                digits['5'] = self.sorted_str(digit)
        for digit in len_5:
            if digit != digits['3'] and digit != digits['5']:
                digits['2'] = self.sorted_str(digit)
        for char in horizontal:
            if char not in ''.join([segments_mapping['a'], segments_mapping['d']]):
                segments_mapping['g'] = char
        result = {digits[key]: key for key in digits}
        return result


if __name__ == '__main__':
    Puzzle().run()
