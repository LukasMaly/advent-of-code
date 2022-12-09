"""
Day 9: Treetop Tree House
https://adventofcode.com/2022/day/9
"""

struct Move
    direction::Char
    steps::Int
end

function parse_moves(lines)
    moves = Vector{Move}()
    for line in lines
        push!(moves, Move(line[1], parse(Int, line[3:end])))
    end
    return moves
end

function simulate(moves; tail_length = 1)
    directions = Dict([('U', [0, 1]), ('D', [0, -1]), ('L', [-1, 0]), ('R', [1, 0])])
    rope = [[0, 0] for i in 1:(tail_length + 1)]
    tail_visited_positions = Set{Vector{Int}}()
    for move in moves
        for _ in range(1, move.steps)
            rope[1] += directions[move.direction]
            for i in range(1, tail_length)
                dist_x, dist_y = rope[i] - rope[i+1]
                if abs(dist_x) >= 2 || abs(dist_y) >= 2
                    rope[i+1][1] += sign(dist_x)
                    rope[i+1][2] += sign(dist_y)
                end
            end
            push!(tail_visited_positions, copy(rope[end]))
        end
    end
    return length(tail_visited_positions)
end

function part1(lines)
    return simulate(parse_moves(lines))
end

function part2(lines)
    return simulate(parse_moves(lines); tail_length = 9)
end

example1 = readlines("examples/09a.txt")
example2 = readlines("examples/09b.txt")
input = readlines("inputs/09.txt")

@assert part1(example1) == 13
println(part1(input))

@assert part2(example2) == 36
println(part2(input))
