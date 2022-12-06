"""
Day 2: Rock Paper Scissors
https://adventofcode.com/2022/day/2
"""

function part1(lines)
    outcome = Dict{String, Dict{String, Int8}}(
        "X" => Dict("A" => 3 + 1,
                    "B" => 0 + 1,
                    "C" => 6 + 1),
        "Y" => Dict("A" => 6 + 2,
                    "B" => 3 + 2,
                    "C" => 0 + 2),
        "Z" => Dict("A" => 0 + 3,
                    "B" => 6 + 3,
                    "C" => 3 + 3)
    )
    rounds = map(line -> split(line, ' '), lines)
    outcomes = map(x -> outcome[x[2]][x[1]], rounds)
    return sum(outcomes)
end

function part2(lines)
    outcome = Dict{String, Dict{String, Int8}}(
        "X" => Dict("A" => 3 + 0,
                    "B" => 1 + 0,
                    "C" => 2 + 0),
        "Y" => Dict("A" => 1 + 3,
                    "B" => 2 + 3,
                    "C" => 3 + 3),
        "Z" => Dict("A" => 2 + 6,
                    "B" => 3 + 6,
                    "C" => 1 + 6)
    )
    rounds = map(line -> split(line, ' '), lines)
    @show rounds
    outcomes = map(x -> outcome[x[2]][x[1]], rounds)
    return sum(outcomes)
end

example = readlines("examples/02.txt")
input = readlines("inputs/02.txt")

@assert part1(example) == 15
println(part1(input))

@assert part2(example) == 12
println(part2(input))
