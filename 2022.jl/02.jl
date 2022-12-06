"""
Day 2: Rock Paper Scissors
https://adventofcode.com/2022/day/2
"""

function part1_outcome(left, right)
    if right == "X"
        if left == "A"
            outcome = 3
        elseif left == "B"
            outcome = 0
        else  # left == "C"
            outcome = 6
        end
        return outcome + 1
    elseif right == "Y"
        if left == "A"
            outcome = 6
        elseif left == "B"
            outcome = 3
        else  # left == "C"
            outcome = 0
        end
        return outcome + 2
    else  # right == "Z"
        if left == "A"
            outcome = 0
        elseif left == "B"
            outcome = 6
        else  # left == "C"
            outcome = 3
        end
        return outcome + 3
    end
end

function part2_outcome(left, right)
    if right == "X"
        if left == "A"
            outcome = 3
        elseif left == "B"
            outcome = 1
        else  # left == "C"
            outcome = 2
        end
        return outcome + 0
    elseif right == "Y"
        if left == "A"
            outcome = 1
        elseif left == "B"
            outcome = 2
        else  # left == "C"
            outcome = 3
        end
        return outcome + 3
    else  # right == "Z"
        if left == "A"
            outcome = 2
        elseif left == "B"
            outcome = 3
        else  # left == "C"
            outcome = 1
        end
        return outcome + 6
    end
end

function part1(lines)
    rounds = map(line -> split(line, ' '), lines)
    outcomes = map(x -> part1_outcome(x[1], x[2]), rounds)
    return sum(outcomes)
end

function part2(lines)
    rounds = map(line -> split(line, ' '), lines)
    outcomes = map(x -> part2_outcome(x[1], x[2]), rounds)
    return sum(outcomes)
end

example = readlines("examples/02.txt")
input = readlines("inputs/02.txt")

@assert part1(example) == 15
println(part1(input))

@assert part2(example) == 12
println(part2(input))
