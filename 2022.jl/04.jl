"""
Day 4: Camp Cleanup
https://adventofcode.com/2022/day/4
"""

function count_overlaps(lines)
    fully_contains = 0
    overlaps = 0

    for line in lines
        m = match(r"(\d+)-(\d+),(\d+)-(\d+)", line)
        a = parse(Int, m[1])
        b = parse(Int, m[2])
        c = parse(Int, m[3])
        d = parse(Int, m[4])
        if a <= c && d <= b
            fully_contains += 1
            overlaps += 1
        elseif c <= a && b <= d
            fully_contains += 1
            overlaps += 1
        elseif a <= c && c <= b
            overlaps += 1
        elseif a <= d && d <= b
            overlaps += 1
        elseif c <= a && a <= d
            overlaps += 1
        elseif c <= b && b <= d
            overlaps += 1
        end
    end
    return fully_contains, overlaps
end

function part1(lines)
    return count_overlaps(lines)[1]
end

function part2(lines)
    return count_overlaps(lines)[2]
end

example = readlines("examples/04.txt")
input = readlines("inputs/04.txt")

@assert part1(example) == 2
println(part1(input))

@assert part2(example) == 4
println(part2(input))
