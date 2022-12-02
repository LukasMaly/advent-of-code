#!/usr/bin/env python3

'''Day 21: Dirac Dice
https://adventofcode.com/2021/day/21
'''

from functools import cache
import itertools

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        positions = self.parse_input(lines)
        scores = [0, 0]
        rolls = 0
        dice = 0
        while (True):
            for player in range(2):
                for d in range(3):
                    dice += 1
                    dice = ((dice - 1) % 100) + 1
                    positions[player] += dice
                    positions[player] = ((positions[player] - 1) % 10) + 1
                scores[player] += positions[player]
                rolls += 3
                if scores[player] >= 1000:
                    return scores[int(not player)] * rolls

    def part2(self, lines: list[str]) -> int:
        positions = self.parse_input(lines)
        wins = self.count_wins(0, positions[0], 0, positions[1], 0)
        return max(wins)

    def parse_input(self, lines: list[str]) -> list[int]:
        player1_start = int(lines[0][-1])
        player2_start = int(lines[1][-1])
        return [player1_start, player2_start]

    def play(self, position: int, score: int, roll: int) -> tuple[int, int]:
        new_position = ((position - 1 + roll) % 10) + 1
        new_score = score + new_position
        return new_position, new_score

    @cache
    def count_wins(self, player: int, pos0: int, score0: int, pos1: int, score1: int) -> list[int]:
        if score0 >= 21:
            return [1, 0]
        elif score1 >= 21:
            return [0, 1]
        wins = [0, 0]
        for rolls in itertools.product(range(1, 4), repeat=3):
            if player == 0:
                new_pos, new_score = self.play(pos0, score0, sum(rolls))
                wins0, wins1 = self.count_wins(1, new_pos, new_score, pos1, score1)
            else:
                new_pos, new_score = self.play(pos1, score1, sum(rolls))
                wins0, wins1 = self.count_wins(0, pos0, score0, new_pos, new_score)
            wins[0] += wins0
            wins[1] += wins1
        return wins


if __name__ == '__main__':
    Puzzle().run()
