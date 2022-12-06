"""
Day 6: Tuning Trouble
https://adventofcode.com/2022/day/6
"""

function detect_marker(line, size)
    for i in size:length(line)
        if length(Set(line[i - size + 1:i])) == size
            return i
        end
    end
end

function part1(lines)
    return detect_marker(lines[1], 4)
end

function part2(lines)
    return detect_marker(lines[1], 14)
end

example = readlines("examples/06.txt")
input = readlines("inputs/06.txt")

@assert part1(example) == 7
println(part1(input))

@assert part2(example) == 19
println(part2(input))
