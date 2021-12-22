#!/usr/bin/env python3

'''Day 20: Trench Map
https://adventofcode.com/2021/day/20
'''

from utils.basepuzzle import BasePuzzle


class Puzzle(BasePuzzle):

    def part1(self, lines: list[str]) -> int:
        algorithm, image = self.parse_input(lines)
        image = self.enhance_image(image, algorithm, 2)
        return sum([sum(row) for row in image])

    def part2(self, lines: list[str]) -> int:
        algorithm, image = self.parse_input(lines)
        image = self.enhance_image(image, algorithm, 50)
        return sum([sum(row) for row in image])

    def parse_input(self, lines: list[str]) -> tuple[list[bool], list[list[bool]]]:
        image_enhancement_algorithm = [True if pixel == "#" else False for pixel in lines[0]]
        input_image = [[True if pixel == "#" else False for pixel in row] for row in lines[2:]]
        return image_enhancement_algorithm, input_image

    def pretty_print(self, image: list[list[bool]]):
        for row in image:
            for pixel in row:
                print("#", end='') if pixel else print(".", end='')
            print()
    
    def enhance_image(self, image: list[list[bool]], algorithm: list[bool], iterations=1) -> list[list[bool]]:
        padding_value = False
        output_image = []
        for i in range(iterations):
            image = self.add_padding(image, padding_value)
            height, width = len(image), len(image[0])
            output_image = [[False] * width for i in range(height)]
            image = self.add_padding(image, padding_value)
            for y in range(1, height + 1):
                for x in range(1, width + 1):
                    number = image[y - 1][x - 1:x + 2] + image[y][x - 1:x + 2] + image[y + 1][x - 1:x + 2]
                    number = "".join(["1" if pixel else "0" for pixel in number])
                    number = int(number, 2)
                    output_image[y - 1][x - 1] = algorithm[number]
            padding_value = algorithm[int("".join(["1" if padding_value == True else "0" for i in range(9)]), 2)]
            image = output_image
        return output_image

    def add_padding(self, image: list[list[bool]], value: bool = False) -> list[list[bool]]:
        for i in range(len(image)):
            image[i] = [value] + image[i] + [value]
        image.insert(0, [value] * len(image[0]))
        image.append([value] * len(image[0]))
        return image


if __name__ == '__main__':
    Puzzle().run()
