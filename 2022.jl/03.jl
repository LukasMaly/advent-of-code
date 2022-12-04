lines = readlines("inputs/03.txt")

# Part 1

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

priorities_sum = sum(priorities)

println(priorities_sum)

# Part 2

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

priorities_sum = sum(priorities)

println(priorities_sum)
