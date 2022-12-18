"""
Day 17: Pyroclastic Flow
https://adventofcode.com/2022/day/17
"""

function parse_input(lines)
    jets = Vector{Int}()
    for char in lines[1]
        if char == '<'
            push!(jets, -1)
        else  # char == '>'
            push!(jets, 1)
        end
    end
    return jets
end

function part1(lines, n_stopped_target)
    jets = parse_input(lines)
    shapes = [[[0, 0], [0, 1], [0, 2], [0, 3]],
              [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]],
              [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]],
              [[0, 0], [1, 0], [2, 0], [3, 0]],
              [[0, 0], [0, 1], [1, 0], [1, 1]]]
    floor = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
    stopped = Vector{Vector{Int}}()
    append!(stopped, floor)
    n_stopped = 0
    height = 0
    i = 0
    j = 0
    while true
        i += 1
        shape = shapes[(i - 1) % length(shapes) + 1]
        rock = map(x -> [x[1] + height + 4, x[2] + 3], shape)
        while true
            if n_stopped == n_stopped_target
                return height
            end
            j += 1
            jet = jets[(j - 1) % length(jets) + 1]  # push by jet
            rock = map(x -> [x[1], x[2] + jet], rock)
            if any(in(map(x -> x[2], rock)), [0, 8])  # hit side
                rock = map(x -> [x[1], x[2] - jet], rock)
            elseif any(in(stopped), rock)  # hit stopped rock
                rock = map(x -> [x[1], x[2] - jet], rock)
            end
            rock = map(x -> [x[1] - 1, x[2]], rock)  # fall
            if any(in(stopped), rock)  # hit stopped rock
                rock = map(x -> [x[1] + 1, x[2]], rock)
                append!(stopped, rock)
                n_stopped += 1
                height = maximum(map(x -> x[1], stopped))
                break
            end
        end
    end
end

function part2(lines, n_stopped_target, search_length)
    jets = parse_input(lines)
    shapes = [[[0, 0], [0, 1], [0, 2], [0, 3]],
              [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]],
              [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]],
              [[0, 0], [1, 0], [2, 0], [3, 0]],
              [[0, 0], [0, 1], [1, 0], [1, 1]]]
    floor = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
    stopped = Vector{Vector{Int}}()
    append!(stopped, floor)
    height_diff = Vector{UInt8}()
    height = 0
    i = 0
    j = 0
    while true
        i += 1
        shape = shapes[(i - 1) % length(shapes) + 1]
        rock = map(x -> [x[1] + height + 4, x[2] + 3], shape)
        while true
            j += 1
            jet = jets[(j - 1) % length(jets) + 1]  # push by jet
            rock = map(x -> [x[1], x[2] + jet], rock)
            if any(in(map(x -> x[2], rock)), [0, 8])  # hit side
                rock = map(x -> [x[1], x[2] - jet], rock)
            elseif any(in(stopped), rock)  # hit stopped rock
                rock = map(x -> [x[1], x[2] - jet], rock)
            end
            rock = map(x -> [x[1] - 1, x[2]], rock)  # fall
            if any(in(stopped), rock)  # hit stopped rock
                rock = map(x -> [x[1] + 1, x[2]], rock)
                append!(stopped, rock)
                previous_height = height
                height = maximum(map(x -> x[1], stopped))
                push!(height_diff, height - previous_height)
                if length(height_diff) > 2 * search_length
                    index = Base._searchindex(height_diff[1:end-search_length], height_diff[end-(search_length-1):end], 1)
                    if index > 0
                        x = map(x -> Int(x), height_diff[1:index-1])
                        y = map(x -> Int(x), height_diff[index:end-search_length])
                        return sum(x) + ((n_stopped_target - length(x)) ÷ length(y)) * sum(y) + sum(y[1:(n_stopped_target - length(x)) % length(y)])
                    end
                end
                break
            end
        end
    end
end

example = readlines("examples/17.txt")
input = readlines("inputs/17.txt")

@assert part1(example, 2022) == 3068
println(part1(example, 2022))

@assert part2(example, 1_000_000_000_000, 20) == 1514285714288
println(part2(input, 1_000_000_000_000, 20))
