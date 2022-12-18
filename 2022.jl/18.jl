"""
Day 18: Boiling Boulders
https://adventofcode.com/2022/day/18
"""

function read_cubes(lines)
    cubes = Vector{Vector{Int}}()
    for line in lines
        y = map(x -> parse(Int, x), split(line, ','))
        push!(cubes, y)
    end
    return hcat(cubes...)
end

function part1(lines)
    cubes = read_cubes(lines)
    grid = zeros(Int, ((maximum(cubes, dims=2) .+ 3)...))
    cubes = cubes .+ 2
    for cube in eachcol(cubes)
        grid[cube...] = 1
    end
    sides = 0
    for dim in [1, 2, 3]
        sides += sum(diff(grid, dims=dim) .!= 0)
    end
    return sides
end

function flood_fill(cube, grid, outer)
    if grid[cube...] == 1 || outer[cube...] == 1
        return
    end
    outer[cube...] = 1
    for dir in [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
        next = cube .+ dir
        grid_size = size(grid)
        if 1 <= next[1] <= grid_size[1] && 1 <= next[2] <= grid_size[2] && 1 <= next[3] <= grid_size[3] 
            flood_fill(next, grid, outer)
        end
    end
end

function part2(lines)
    cubes = read_cubes(lines)
    grid = zeros(Int, ((maximum(cubes, dims=2) .+ 3)...))
    outer = zeros(Int, ((maximum(cubes, dims=2) .+ 3)...))
    cubes = cubes .+ 2
    for cube in eachcol(cubes)
        grid[cube...] = 1
    end
    flood_fill([1, 1, 1], grid, outer)
    sides = 0
    for dim in [1, 2, 3]
        sides += sum(diff(outer, dims=dim) .!= 0)
    end
    return sides
end

example = readlines("examples/18.txt")
input = readlines("inputs/18.txt")

@assert part1(example) == 64
println(part1(input))

@assert part2(example) == 58
println(part2(input))
