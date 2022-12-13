"""
Day 12: Hill Climbing Algorithm
https://adventofcode.com/2022/day/12
"""

function part1(lines)
    heightmap = reduce(vcat, permutedims.(collect.(lines)))
    m, n = size(heightmap)
    start = collect(Tuple(findall(x -> x == 'S', heightmap)[1]))
    heightmap[start...] = Char(Int('a') - 1)
    finish = collect(Tuple(findall(x -> x == 'E', heightmap)[1]))
    heightmap[finish...] = Char(Int('z') + 1)
    distances = Vector{Matrix{Int}}()
    push!(distances, vcat(zeros(Int, (1, n)), diff(heightmap, dims=1)))
    push!(distances, vcat(reverse(diff(reverse(heightmap), dims=1)), zeros(Int, (1, n))))
    push!(distances, hcat(zeros(Int, (m, 1)), diff(heightmap, dims=2)))
    push!(distances, hcat(reverse(diff(reverse(heightmap), dims=2)), zeros(Int, (m, 1))))
    for distance in distances
        distance[distance .< 1] .= 1
        distance[distance .> 1] .= typemax(Int) - m * n
    end
    # Dijkstra's algorithm
    m, n = size(distances[1])
    dist = ones(Int, (m, n)) .* (typemax(Int) - m * n)
    dist[start...] = 0
    visited = zeros(Bool, (m, n))
    pos = copy(start)
    while true
        for (i, delta) in enumerate([[1, 0], [-1, 0], [0, 1], [0, -1]])
            new_pos = pos + delta
            if 1 <= new_pos[1] <= m && 1 <= new_pos[2] <= n
                if !visited[new_pos...] && dist[new_pos...] > distances[i][new_pos...] + dist[pos...]
                    dist[new_pos...] = distances[i][new_pos...] + dist[pos...]
                end
            end
        end
        visited[pos...] = true
        dist[pos...] = typemax(Int) - m * n
        pos = collect(Tuple(findmin(dist)[2]))
        if pos == finish
            break
        end
    end
    return dist[pos...]
end

function part2(lines)
    heightmap = reduce(vcat, permutedims.(collect.(lines)))
    m, n = size(heightmap)
    start = collect(Tuple(findall(x -> x == 'E', heightmap)[1]))
    heightmap[start...] = Char(Int('z') + 1)
    distances = Vector{Matrix{Int}}()
    push!(distances, vcat(zeros(Int, (1, n)), reverse(diff(reverse(heightmap), dims=1))))
    push!(distances, vcat(diff(heightmap, dims=1), zeros(Int, (1, n))))
    push!(distances, hcat(zeros(Int, (m, 1)), reverse(diff(reverse(heightmap), dims=2))))
    push!(distances, hcat(diff(heightmap, dims=2), zeros(Int, (m, 1))))
    for distance in distances
        distance[distance .< 1] .= 1
        distance[distance .> 1] .= typemax(Int) - m * n
    end
    # Dijkstra's algorithm
    m, n = size(distances[1])
    dist = ones(Int, (m, n)) .* (typemax(Int) - m * n)
    dist[start...] = 0
    visited = zeros(Bool, (m, n))
    pos = copy(start)
    while true
        for (i, delta) in enumerate([[1, 0], [-1, 0], [0, 1], [0, -1]])
            new_pos = pos + delta
            if 1 <= new_pos[1] <= m && 1 <= new_pos[2] <= n
                if !visited[new_pos...] && dist[new_pos...] > distances[i][new_pos...] + dist[pos...]
                    dist[new_pos...] = distances[i][new_pos...] + dist[pos...]
                end
            end
        end
        visited[pos...] = true
        dist[pos...] = typemax(Int) - m * n
        pos = collect(Tuple(findmin(dist)[2]))
        if heightmap[pos...] == 'a'
            break
        end
    end
    return dist[pos...]
end

example = readlines("examples/12.txt")
input = readlines("inputs/12.txt")

@assert part1(example) == 31
println(part1(input))

@assert part2(example) == 29
println(part2(input))
