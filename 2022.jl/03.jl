"""
Day 3: Rucksack Reorganization
https://adventofcode.com/2022/day/3
"""

function part1(lines)
    priorities = Vector{Int}()

    for line in lines
        first_compartment = line[1:length(line)÷2]
        second_compartment = line[length(line)÷2+1:end]
        letter = intersect(first_compartment, second_compartment)[1]
        priority = Int(letter)
        if priority > 96
            priority -= 96
        else
            priority -= 38
        end
        push!(priorities, priority)
    end

    return sum(priorities)
end

function part2(lines)
    priorities = Vector{Int}()

    for i in 1:3:length(lines)
        letter = intersect(lines[i], intersect(lines[i+1], lines[i+2]))[1]
        priority = Int(letter)
        if priority > 96
            priority -= 96
        else
            priority -= 38
        end
        push!(priorities, priority)
    end

    return sum(priorities)
end

example = readlines("examples/03.txt")
input = readlines("inputs/03.txt")

@assert part1(example) == 157
println(part1(input))

@assert part2(example) == 70
println(part2(input))
