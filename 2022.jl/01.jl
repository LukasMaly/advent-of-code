lines = readlines("inputs/01.txt")

# Part 1

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

sums = map(elf -> sum(elf), elves)

println(maximum(sums))

# Part 2

top_three = partialsortperm(sums, 1:3, rev=true)
top_three_sum = sum(sums[top_three])

println(top_three_sum)
