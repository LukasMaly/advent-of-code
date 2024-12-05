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
                    if update[i] in rules:
                        if update[i+1] in rules[update[i]]:
                            found = True
                    if not found:
                        update[i], update[i+1] = update[i+1], update[i]
            corrected_updates.append(update)
        return self.middle_pages_sum(corrected_updates)

    def parse_input(self, lines: list[str]) -> tuple[dict[int, list[int]], list[list[int]]]:
        rules = {}
        updates = []
        for line in lines:
            if '|' in line:
                x, y = line.split('|')
                x, y = int(x), int(y)
                if x in rules:
                    rules[x].append(y)
                else:
                    rules[x] = [y]
            elif ',' in line:
                pages = line.split(',')
                updates.append([int(p) for p in pages])
        return rules, updates

    def is_correctly_ordered(self, update: list[int], rules: dict[int, list[int]]) -> bool:
        for i in range(len(update) - 1):
            if update[i] not in rules:
                return False
            for next_page in update[i+1:]:
                if next_page not in rules[update[i]]:
                    return False
        return True

    def middle_pages_sum(self, updates: list[list[int]]) -> int:
        middle_page_numbers = []
        for update in updates:
            middle_page_numbers.append(update[len(update) // 2])
        return sum(middle_page_numbers)


if __name__ == '__main__':
    Puzzle().run()
