"""
Day 14: Regolith Reservoir
https://adventofcode.com/2022/day/14
"""

function read_paths(lines)
    paths = Vector{Vector{Vector{Int}}}()
    for line in lines
        path = Vector{Vector{Int}}()
        coordinates = split(line, " -> ")
        for coords in coordinates
            push!(path, map(x -> parse(Int, x), split(coords, ',')))
        end
        push!(paths, path)
    end
    return paths
end

function get_rocks(paths)
    rocks = Set{Vector{Int}}()
    for path in paths
        for n in 1:(length(path) - 1)
            i1 = min(path[n][2], path[n + 1][2])
            i2 = max(path[n][2], path[n + 1][2])
            j1 = min(path[n][1], path[n + 1][1])
            j2 = max(path[n][1], path[n + 1][1])
            if i1 == i2
                for j in j1:j2
                    push!(rocks, [i1, j])
                end
            else  # j1 == j2
                for i in i1:i2
                    push!(rocks, [i, j1])
                end
            end
        end
    end
    return rocks
end

function part1(lines)
    paths = read_paths(lines)
    left = minimum([coords[1] for path in paths for coords in path])
    right = maximum([coords[1] for path in paths for coords in path])
    bottom = maximum([coords[2] for path in paths for coords in path])
    rocks = get_rocks(paths)
    sand = Set{Vector{Int}}()
    done = false
    while !done
        pos = [0, 500]
        while true
            if (pos + [1, 0]) ∉ rocks && (pos + [1, 0]) ∉ sand
                pos += [1, 0]
            elseif (pos + [1, -1]) ∉ rocks && (pos + [1, -1]) ∉ sand
                pos += [1, -1]
            elseif (pos + [1, 1]) ∉ rocks && (pos + [1, 1]) ∉ sand
                pos += [1, 1]
            else
                push!(sand, pos)
                break
            end
            if pos[1] > bottom || pos[2] < left || pos[2] > right
                done = true
                break
            end
        end
    end
    return length(sand)
end

function part2(lines)
    paths = read_paths(lines)
    bottom = maximum([coords[2] for path in paths for coords in path])
    floor = bottom + 2
    rocks = get_rocks(paths)
    sand = Set{Vector{Int}}()
    done = false
    while !done
        pos = [0, 500]
        while true
            if (pos + [1, 0]) ∉ rocks && (pos + [1, 0]) ∉ sand
                pos += [1, 0]
            elseif (pos + [1, -1]) ∉ rocks && (pos + [1, -1]) ∉ sand
                pos += [1, -1]
            elseif (pos + [1, 1]) ∉ rocks && (pos + [1, 1]) ∉ sand
                pos += [1, 1]
            else
                if pos == [0, 500]
                    done = true
                end
                push!(sand, pos)
                break
            end
            if pos[1] == floor - 1
                push!(sand, pos)
                break
            end
        end
    end
    return length(sand)
end

example = readlines("examples/14.txt")
input = readlines("inputs/14.txt")

@assert part1(example) == 24
println(part1(input))

@assert part2(example) == 93
println(part2(input))
