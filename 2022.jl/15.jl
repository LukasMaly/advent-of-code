"""
Day 15: Beacon Exclusion Zone
https://adventofcode.com/2022/day/15
"""

function parse_input(lines)
    sensors = Vector{Vector{Int}}()
    beacons = Vector{Vector{Int}}()
    for line in lines
        m = match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
        sx = parse(Int, m[1])
        sy = parse(Int, m[2])
        bx = parse(Int, m[3])
        by = parse(Int, m[4])
        push!(sensors, [sx, sy])
        push!(beacons, [bx, by])
    end
    return (sensors, beacons)
end

function part1(lines, y)
    (sensors, beacons) = parse_input(lines)
    positions = Set{Int}()
    distances = Vector{Int}()
    for (sensor, beacon) in zip(sensors, beacons)
        distance = abs(sensor[1] - beacon[1]) + abs(sensor[2] - beacon[2])
        if sensor[2] - distance <= y <= sensor[2] + distance
            n = abs(y - sensor[2])
            for x in (sensor[1] - (distance - n)):(sensor[1] + (distance - n))
                push!(positions, x)
            end
        end
    end
    for beacon in beacons
        if beacon[2] == y
            delete!(positions, beacon[1])
        end
    end
    return length(positions)
end

function lines_intersection(line1, line2)
    a1 = line1[2][2] - line1[1][2]
    b1 = line1[1][1] - line1[2][1]
    c1 = a1 * line1[1][1] + b1 * line1[1][2]
    a2 = line2[2][2] - line2[1][2]
    b2 = line2[1][1] - line2[2][1]
    c2 = a2 * line2[1][1] + b2 * line2[1][2]
    det = a1 * b2 - a2 * b1
    if det == 0
        return nothing
    else
        x = (b2 * c1 - b1 * c2) / det
        y = (a1 * c2 - a2 * c1) / det
        return (Int(round(x)), Int(round(y)))
    end
end

struct Vertices
    left::Tuple{Int, Int}
    right::Tuple{Int, Int}
    top::Tuple{Int, Int}
    bottom::Tuple{Int, Int}
end

function part2(lines, n)
    (sensors, beacons) = parse_input(lines)
    sensors = hcat(sensors...)
    beacons = hcat(beacons...)
    distances = abs.(sensors[1, :] .- beacons[1, :]) .+ abs.(sensors[2, :] .- beacons[2, :])
    vertices = Vector{Vertices}()
    n_sensors = size(sensors)[2]
    for i in 1:n_sensors
        left = Tuple(sensors[:, i] + [-(distances[i]+1), 0])
        right = Tuple(sensors[:, i] + [distances[i]+1, 0])
        top = Tuple(sensors[:, i] + [0, -(distances[i]+1)])
        bottom = Tuple(sensors[:, i] + [0, distances[i]+1])
        push!(vertices, Vertices(left, right, top, bottom))
    end
    for i in 1:n_sensors-1
        for j in i+1:n_sensors
            intersections = []
            push!(intersections, lines_intersection((vertices[i].top, vertices[i].right), (vertices[j].right, vertices[j].bottom)))
            push!(intersections, lines_intersection((vertices[i].top, vertices[i].right), (vertices[j].left, vertices[j].top)))
            push!(intersections, lines_intersection((vertices[i].bottom, vertices[i].left), (vertices[j].right, vertices[j].bottom)))
            push!(intersections, lines_intersection((vertices[i].bottom, vertices[i].left), (vertices[j].left, vertices[j].top)))
            push!(intersections, lines_intersection((vertices[i].right, vertices[i].bottom), (vertices[j].top, vertices[j].right)))
            push!(intersections, lines_intersection((vertices[i].right, vertices[i].bottom), (vertices[j].bottom, vertices[j].left)))
            push!(intersections, lines_intersection((vertices[i].left, vertices[i].top), (vertices[j].top, vertices[j].right)))
            push!(intersections, lines_intersection((vertices[i].left, vertices[i].top), (vertices[j].bottom, vertices[j].left)))
            for intersection in intersections
                if !isnothing(intersection)
                    (x, y) = intersection
                    if 0 <= x <= n && 0 <= y <= n
                        if sum(abs.(x .- sensors[1, :]) .+ abs.(y .- sensors[2, :]) .> distances) == n_sensors
                            return x * 4_000_000 + y
                        end
                    end
                end
            end
        end
    end
end

example = readlines("examples/15.txt")
input = readlines("inputs/15.txt")

@assert part1(example, 10) == 26
println(part1(input, 2_000_000))

@assert part2(example, 20) == 56000011
println(part2(input, 4_000_000))
