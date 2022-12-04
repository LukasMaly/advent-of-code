lines = readlines("inputs/02.txt")

# Part 1

function part1(left, right)
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

rounds = map(line -> split(line, ' '), lines)
outcomes = map(x -> part1(x[1], x[2]), rounds)
total_score = sum(outcomes)

println(total_score)

# Part 2

function part2(left, right)
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

outcomes = map(x -> part2(x[1], x[2]), rounds)
total_score = sum(outcomes)

println(total_score)
