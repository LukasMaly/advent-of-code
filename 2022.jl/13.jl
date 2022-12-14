"""
Day 13: Distress Signal
https://adventofcode.com/2022/day/13
"""

function is_right_order(a, b)
    for (left, right) in zip(a, b)
        if left isa Int && right isa Int
            if left == right
                continue
            elseif left > right
                return false
            else
                return true
            end
        elseif left isa Vector && right isa Vector
            result = is_right_order(left, right)
            if isnothing(result)
                continue
            else
                return(result)
            end
        else
            if left isa Int
                result = is_right_order([left], right)
            else
                result = is_right_order(left, [right])
            end
            if isnothing(result)
                continue
            else
                return(result)
            end
        end
    end
    if length(a) < length(b)
        return true
    elseif length(a) > length(b)
        return false
    else
        return nothing
    end
end

function part1(lines)
    n_pairs = (length(lines) + 1) ÷ 3
    right_orders = Vector{Bool}()
    for i in 1:n_pairs
        a = eval(Meta.parse(lines[i * 3 - 2]))
        b = eval(Meta.parse(lines[i * 3 - 1]))
        result = is_right_order(a, b)
        push!(right_orders, result)
    end
    return sum(right_orders .* collect(1:n_pairs))
end

function part2(lines)
    unordered = Vector{Vector}()
    n_pairs = (length(lines) + 1) ÷ 3
    for i in 1:n_pairs
        push!(unordered, eval(Meta.parse(lines[i * 3 - 2])))
        push!(unordered, eval(Meta.parse(lines[i * 3 - 1])))
    end
    push!(unordered, [[2]])
    push!(unordered, [[6]])
    ordered = Vector{Vector}()
    push!(ordered, popfirst!(unordered))
    while length(unordered) > 0
        item = popfirst!(unordered)
        inserted = false
        for i in 1:length(ordered)
            if is_right_order(item, ordered[i])
                insert!(ordered, i, item)
                inserted = true
                break
            end
        end
        if !inserted
            push!(ordered, item)
        end
    end
    return prod(findall(x -> x == [[2]] || x == [[6]], ordered))
end

example = readlines("examples/13.txt")
input = readlines("inputs/13.txt")

@assert part1(example) == 13
println(part1(input))

@assert part2(example) == 140
println(part2(input))
