#!/usr/bin/env python3

'''Day 10: Syntax Scoring
https://adventofcode.com/2021/day/10
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    PAIRS = {')': '(', ']': '[', '}': '{', '>': '<'}
    OPENING = ['(', '[', '{', '<']

    def part1(self, lines: list[str]) -> int:
        POINTS = {')': 3,
                  ']': 57,
                  '}': 1197,
                  '>': 25137}
        illegals = []
        for line in lines:
            opened = []
            for char in line:
                if char in self.OPENING:
                    opened.append(char)
                else:
                    if opened[-1] == self.PAIRS[char]:
                        del opened[-1]
                    else:
                        illegals.append(char)
                        break
        score = sum([POINTS[illegal] for illegal in illegals])
        return score

    def part2(self, lines: list[str]) -> int:
        POINTS = {'(': 1,
                  '[': 2,
                  '{': 3,
                  '<': 4}
        scores = []
        for line in lines:
            opened = []
            corrupted = False
            for char in line:
                if char in self.OPENING:
                    opened.append(char)
                else:
                    if opened[-1] == self.PAIRS[char]:
                        del opened[-1]
                    else:
                        corrupted = True
                        break
            if not corrupted:
                score = 0
                for char in reversed(opened):
                    score *= 5
                    score += POINTS[char]
                scores.append(score)
        scores = sorted(scores)
        result = scores[len(scores) // 2]
        return result

if __name__ == '__main__':
    Puzzle().run()
