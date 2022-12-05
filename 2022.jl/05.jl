lines = readlines("inputs/05.txt")

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

stacks = read_stacks(lines)
rearrangements = read_rearrangements(lines)

# Part 1

function part1(stacks, rearrangements)
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

top = part1(copy(stacks), copy(rearrangements))

println(top)

# Part 2

function part2(stacks, rearrangements)
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

top = part2(copy(stacks), copy(rearrangements))

println(top)
