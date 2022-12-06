"""
Day 1: Rock Paper Scissors
https://adventofcode.com/2022/day/1
"""

function calories_sums(lines)
    elves = Vector{Vector{Int64}}()
    elf = Vector{Int64}()
    for line in lines
        if line == ""
            push!(elves, copy(elf))
            empty!(elf)
        else
            calories = parse(Int64, line)
            push!(elf, calories)
        end
    end
    push!(elves, elf)
    return map(elf -> sum(elf), elves)
end

function part1(lines)
    sums = calories_sums(lines)
    return maximum(sums)
end

function part2(lines)
    sums = calories_sums(lines)
    top_three = partialsortperm(sums, 1:3, rev=true)
    return sum(sums[top_three])
end

example = readlines("examples/01.txt")
input = readlines("inputs/01.txt")

@assert part1(example) == 24000
println(part1(input))

@assert part2(example) == 45000
println(part2(input))
