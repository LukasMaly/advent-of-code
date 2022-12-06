"""
Day 5: Supply Stacks
https://adventofcode.com/2022/day/5
"""

function read_stacks(lines)
    empty_line = findall(isempty, lines)[1]
    n_stacks = parse(Int, lines[empty_line - 1][end - 1])
    stacks = Vector{String}()
    for i in 1:n_stacks
        stack = ""
        for line in lines[(empty_line - 2):-1:1]
            crate = line[i * 4 - 2]
            if !isspace(crate)
                stack = stack * crate
            else
                break
            end
        end
        push!(stacks, stack)
    end
    return stacks
end

function read_rearrangements(lines)
    empty_line = findall(isempty, lines)[1]
    rearrangements = Vector{Vector{Int}}()
    for line in lines[empty_line+1:end]
        rearrangement = Vector{Int}()
        m = match(r"move (\d+) from (\d+) to (\d+)", line)
        for i in 1:3
            push!(rearrangement, parse(Int, m[i]))
        end
        push!(rearrangements, rearrangement)
    end
    return rearrangements
end

function part1(lines)
    stacks = read_stacks(lines)
    rearrangements = read_rearrangements(lines)
    for rearrangement in rearrangements
        for i in 1:rearrangement[1]
            stacks[rearrangement[3]] *= stacks[rearrangement[2]][end]
            stacks[rearrangement[2]] = stacks[rearrangement[2]][1:end-1]
        end
    end
    top = ""
    for stack in stacks
        top *= stack[end]
    end
    return top
end

function part2(lines)
    stacks = read_stacks(lines)
    rearrangements = read_rearrangements(lines)
    for rearrangement in rearrangements
        stacks[rearrangement[3]] *= stacks[rearrangement[2]][(end-rearrangement[1]+1):end]
        stacks[rearrangement[2]] = stacks[rearrangement[2]][1:(end-rearrangement[1])]
    end
    top = ""
    for stack in stacks
        top *= stack[end]
    end
    return top
end

example = readlines("examples/05.txt")
input = readlines("inputs/05.txt")

@assert part1(example) == "CMZ"
println(part1(input))

@assert part2(example) == "MCD"
println(part2(input))
