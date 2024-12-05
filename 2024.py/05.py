#!/usr/bin/env python3

'''Day 5: Print Queue
https://adventofcode.com/2024/day/5
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        rules, updates = self.parse_input(lines)
        correct_updates = []
        for update in updates:
            if self.is_correctly_ordered(update, rules):
                correct_updates.append(update)
        return self.middle_pages_sum(correct_updates)

    def part2(self, lines: list[str]) -> int:
        rules, updates = self.parse_input(lines)
        not_correct_updates = []
        for update in updates:
            if not self.is_correctly_ordered(update, rules):
                not_correct_updates.append(update)
        corrected_updates = []
        for update in not_correct_updates:
            while not self.is_correctly_ordered(update, rules):
                for i in range(len(update) - 1):
                    found = False
                    for rule in rules:
                        if update[i] == rule[0]:
                            if update[i+1] == rule[1]:
                                found = True
                                break
                    if not found:
                        update[i], update[i+1] = update[i+1], update[i]
            corrected_updates.append(update)
        return self.middle_pages_sum(corrected_updates)

    def parse_input(self, lines: list[str]) -> tuple[list[tuple[int, int]], list[list[int]]]:
        rules = []
        updates = []
        for line in lines:
            if '|' in line:
                x, y = line.split('|')
                rules.append((int(x), int(y)))
            elif ',' in line:
                pages = line.split(',')
                updates.append([int(p) for p in pages])
        return rules, updates

    def is_correctly_ordered(self, update: list[int], rules: list[tuple[int, int]]) -> bool:
        for i in range(len(update) - 1):
            found = 0
            for rule in rules:
                if update[i] == rule[0]:
                    for next_page in update[i+1:]:
                        if next_page == rule[1]:
                            found += 1
                            break
            if found != len(update) - i - 1:
                return False
        return True

    def middle_pages_sum(self, updates: list[list[int]]) -> int:
        middle_page_numbers = []
        for update in updates:
            middle_page_numbers.append(update[len(update) // 2])
        return sum(middle_page_numbers)


if __name__ == '__main__':
    Puzzle().run()
