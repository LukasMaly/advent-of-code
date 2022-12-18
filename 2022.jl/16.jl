"""
Day 16: Proboscidea Volcanium
https://adventofcode.com/2022/day/16
"""

mutable struct Valve
    flow_rate::Int
    tunnels::Vector{String}
end

function parse_input(lines)
    valves = Dict{String, Valve}()
    for line in lines
        m = match(r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? (.*)", line)
        valve = m[1]
        flow_rate = parse(Int, m[2])
        tunnels = Vector{String}()
        for tunnel in split(m[3], ", ")
            push!(tunnels, tunnel)
        end
        valves[valve] = Valve(flow_rate, tunnels)
    end
    return valves
end

function floyd_warshall(valves)
    distances = Dict{String, Dict{String, Int}}()
    for u in keys(valves)
        distances[u] = Dict{String, Int}()
        for v in keys(valves)
            distances[u][v] = 999_999
        end
    end
    for (u, valve) in valves
        for v in valve.tunnels
            distances[u][v] = 1
        end
    end
    for u in keys(valves)
        distances[u][u] = 0
    end
    for k in keys(valves)
        for i in keys(valves)
            for j in keys(valves)
                if distances[i][j] > distances[i][k] + distances[k][j]
                    distances[i][j] = distances[i][k] + distances[k][j]
                end
            end
        end
    end
    return distances
end

function move(valves, distances, pressure_release, path, valve, distance, total_release, remaining_minutes)
    if distance >= remaining_minutes - 1
        return
    end
    push!(path, valve)
    remaining_minutes -= distance + 1
    total_release += valves[valve].flow_rate * remaining_minutes
    pressure_release[path] = total_release
    for (valve, distance) in distances[valve]
        if valve ∉ path
            move(valves, distances, pressure_release, copy(path), valve, distance, total_release, remaining_minutes)
        end
    end
end

function part1(lines)
    valves = parse_input(lines)
    distances = floyd_warshall(valves)
    zero_flow_valves = [k for (k, v) in valves if v.flow_rate == 0]
    # delete itself
    for u in keys(distances)
        delete!(distances[u], u)
    end
    # delete zero flow valves from targets
    for u in keys(distances)
        for v in zero_flow_valves
            delete!(distances[u], v)
        end
    end
    # delete zero flow valves from sources
    for v in zero_flow_valves
        if v != "AA"
            delete!(distances, v)
        end
        delete!(valves, v)
    end
    pressure_release = Dict{Vector{String}, Int}()
    path = Vector{String}()
    for (valve, distance) in distances["AA"]
        move(valves, distances, pressure_release, copy(path), valve, distance, 0, 30)
    end
    return maximum(values(pressure_release))
end

function part2(lines)
    valves = parse_input(lines)
    distances = floyd_warshall(valves)
    zero_flow_valves = [k for (k, v) in valves if v.flow_rate == 0]
    # delete itself
    for u in keys(distances)
        delete!(distances[u], u)
    end
    # delete zero flow valves from targets
    for u in keys(distances)
        for v in zero_flow_valves
            delete!(distances[u], v)
        end
    end
    # delete zero flow valves from sources
    for v in zero_flow_valves
        if v != "AA"
            delete!(distances, v)
        end
        delete!(valves, v)
    end
    pressure_release = Dict{Vector{String}, Int}()
    path = Vector{String}()
    for (valve, distance) in distances["AA"]
        move(valves, distances, pressure_release, copy(path), valve, distance, 0, 26)
    end
    with_elephant = 0
    for (i, key1) in enumerate(collect(keys(pressure_release))[1:end-1])
        for key2 in collect(keys(pressure_release))[i+1:end]
            if !any(in(key1), key2)
                with_elephant = max(with_elephant, pressure_release[key1] + pressure_release[key2])
            end
        end
    end
    return with_elephant
end

example = readlines("examples/16.txt")
input = readlines("inputs/16.txt")

@assert part1(example) == 1651
println(part1(input))

@assert part2(example) == 1707
println(part2(input))
