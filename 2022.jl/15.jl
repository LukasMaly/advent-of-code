"""
Day 15: 
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

function part2(lines, n)
    (sensors, beacons) = parse_input(lines)
    sensors = hcat(sensors...)
    beacons = hcat(beacons...)
    distances = abs.(sensors[1, :] .- beacons[1, :]) .+ abs.(sensors[2, :] .- beacons[2, :])
    boundaries = Vector{Set{Tuple{Int, Int}}}()
    for i in 1:size(sensors)[2]
        top = sensors[:, i] + [0, -(distances[i]+1)]
        bottom = sensors[:, i] + [0, distances[i]+1]
        left = sensors[:, i] + [-(distances[i]+1), 0]
        right = sensors[:, i] + [distances[i]+1, 0]
        boundary = Set{Tuple{Int, Int}}()
        for (x, y) in zip(top[1]:right[1], top[2]:right[2])
            if 0 <= x <= n && 0 <= y <= n
                push!(boundary, (x, y))
            end
        end
        for (x, y) in zip(right[1]:-1:bottom[1], right[2]:bottom[2])
            if 0 <= x <= n && 0 <= y <= n
                push!(boundary, (x, y))
            end
        end
        for (x, y) in zip(bottom[1]:-1:left[1], bottom[2]:-1:left[2])
            if 0 <= x <= n && 0 <= y <= n
                push!(boundary, (x, y))
            end
        end
        for (x, y) in zip(left[1]:top[1], left[2]:-1:top[2])
            if 0 <= x <= n && 0 <= y <= n
                push!(boundary, (x, y))
            end
        end
        push!(boundaries, boundary)
    end
    for i in 1:length(boundaries)-1
        for j in i+1:length(boundaries)
            intersections = intersect(boundaries[i], boundaries[j])
            for intersection in intersections
                (x, y) = intersection
                m = 0
                for n in 1:size(sensors)[2]
                    if abs(x - sensors[1, n]) + abs(y - sensors[2, n]) > distances[n]
                        m += 1
                    end
                end
                if m == size(sensors)[2]
                    return x * 4_000_000 + y
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
