"""
Day 8: Treetop Tree House
https://adventofcode.com/2022/day/8
"""

function read_map(lines)
    return reduce(vcat, [map(x -> parse(Int, x), collect(line)) for line in lines]')
end

function part1(lines)
    height_map = read_map(lines)
    m, n = size(height_map)
    visibility_map = zeros(Bool, (m, n))
    for j = 1:n
        max_height1 = height_map[1, j]
        visibility_map[1, j] = true
        max_height2 = height_map[end, j]
        visibility_map[end, j] = true
        for (i1, i2) in zip(2:m-1, m-1:-1:2)
            if height_map[i1, j] > max_height1
                visibility_map[i1, j] = true
                max_height1 = height_map[i1, j]
            end
            if height_map[i2, j] > max_height2
                visibility_map[i2, j] = true
                max_height2 = height_map[i2, j]
            end
        end
    end
    for i = 1:m
        max_height1 = height_map[i, 1]
        visibility_map[i, 1] = true
        max_height2 = height_map[i, end]
        visibility_map[i, end] = true
        for (j1, j2) in zip(2:n-1, n-1:-1:2)
            if height_map[i, j1] > max_height1
                visibility_map[i, j1] = true
                max_height1 = height_map[i, j1]
            end
            if height_map[i, j2] > max_height2
                visibility_map[i, j2] = true
                max_height2 = height_map[i, j2]
            end
        end
    end
    return sum(visibility_map)
end

function part2(lines)
    height_map = read_map(lines)
    m, n = size(height_map)
    score_map = zeros(Int, (m, n))
    for j = 2:n-1
        for i = 2:m-1
            score = 1
            height = height_map[i, j]
            # Up
            view = 0
            for y = i-1:-1:1
                view += 1
                if height_map[y, j] >= height
                    break
                end
            end
            score *= view
            # Left
            view = 0
            for x = j-1:-1:1
                view += 1
                if height_map[i, x] >= height
                    break
                end
            end
            score *= view
            # Right
            view = 0
            for x = j+1:n
                view += 1
                if height_map[i, x] >= height
                    break
                end
            end
            score *= view
            # Down
            view = 0
            for y = i+1:m
                view += 1
                if height_map[y, j] >= height
                    break
                end
            end
            score *= view
            score_map[i, j] = score
        end
    end
    return maximum(score_map)
end

example = readlines("examples/08.txt")
input = readlines("inputs/08.txt")

@assert part1(example) == 21
println(part1(input))

@assert part2(example) == 8
println(part2(input))
