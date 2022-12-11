"""
Day 11: Monkey in the Middle
https://adventofcode.com/2022/day/11
"""

mutable struct Monkey
    items::Vector{Int}
    operation
    test
    divisor
    inspections::Int
end

function parse_input(lines)
    monkeys = Vector{Monkey}()
    for n in range(1, (length(lines) + 1) ÷ 7)
        i = ((n - 1) * 7 + 1)
        items = map(x -> parse(Int, x), split(lines[i + 1][19:end], ", "))
        if lines[i + 2][24] == '+'
            if lines[i + 2][26] == 'o'
                operation = x -> x + x
            else
                term = parse(Int, lines[i + 2][26:end])
                operation = x -> x + term
            end
        else
            if lines[i + 2][26] == 'o'
                operation = x -> x * x
            else
                factor = parse(Int, lines[i + 2][26:end])
                operation = x -> x * factor
            end
        end
        divisor = parse(Int, lines[i + 3][22:end])
        true_monkey_id = parse(Int, lines[i + 4][30:end])
        false_mokey_id = parse(Int, lines[i + 5][31:end])
        test = x -> (x % divisor) == 0 ? true_monkey_id : false_mokey_id
        monkey = Monkey(items, operation, test, divisor, 0)
        push!(monkeys, monkey)
    end
    return monkeys
end

function part1(lines)
    monkeys = parse_input(lines)
    for _ in range(1, 20)
        for monkey in monkeys
            while length(monkey.items) > 0
                item = popfirst!(monkey.items)
                item = monkey.operation(item)
                item = Int(floor(item / 3))
                result = monkey.test(item)
                push!(monkeys[result + 1].items, item)
                monkey.inspections += 1
            end
        end
    end
    inspections = map(monkey -> monkey.inspections, monkeys)
    top_two = sort(inspections, rev=true)[1:2]
    return prod(top_two)
end

function part2(lines)
    monkeys = parse_input(lines)
    divisors_prod = prod(map(monkey -> monkey.divisor, monkeys))
    for _ in range(1, 10_000)
        for monkey in monkeys
            while length(monkey.items) > 0
                item = popfirst!(monkey.items)
                item = monkey.operation(item) % divisors_prod
                result = monkey.test(item)
                push!(monkeys[result + 1].items, item)
                monkey.inspections += 1
            end
        end
    end
    inspections = map(monkey -> monkey.inspections, monkeys)
    top_two = sort(inspections, rev=true)[1:2]
    return prod(top_two)
end

example = readlines("examples/11.txt")
input = readlines("inputs/11.txt")

@assert part1(example) == 10605
println(part1(input))

@assert part2(example) == 2713310158
println(part2(input))
