"""
Day 7: No Space Left On Device
https://adventofcode.com/2022/day/7
"""

function list_files(lines)
    files = Vector{Tuple{String, String, Int}}()
    path = "/"
    for line in lines[3:end]
        if startswith(line, '$')
            if startswith(line, "\$ cd")
                dir = split(line)[3]
                if dir == ".."           
                    if length(begin parts = splitpath(path) end) > 2
                        path = joinpath(parts[1:end-1])
                    else
                        path = "/"
                    end
                else
                    path = joinpath(path, dir)
                end
            end
            continue
        elseif startswith(line, "dir")
            continue
        else
            m = match(r"(\d+) (.*)", line)
            size = parse(Int, m[1])
            name = m[2]
            push!(files, ("$path", "$name", size))
        end
    end
    return files
end

function get_dir_sizes(files)
    dir_sizes = Dict{String, Int}()
    for file in files
        path = file[1]
        size = file[3]
        if !haskey(dir_sizes, path)
            dir_sizes[path] = size
        else
            dir_sizes[path] += size
        end
        while length(begin parts = splitpath(path) end) > 1
            path = joinpath(parts[1:end-1])
            if !haskey(dir_sizes, path)
                dir_sizes[path] = size
            else
                dir_sizes[path] += size
            end
        end
    end
    return dir_sizes
end

function part1(lines)
    files = list_files(lines)
    dir_sizes = get_dir_sizes(files)
    below_100000 = filter(p -> p[2] < 100_000, dir_sizes)
    return sum(collect(values(below_100000)))
end

function part2(lines)
    available_space = 70_000_000
    required_space = 30_000_000
    files = list_files(lines)
    dir_sizes = get_dir_sizes(files)
    used_space = dir_sizes["/"]
    unused_space = available_space - used_space
    required_size = required_space - unused_space
    dir_sizes = sort(collect(values(dir_sizes)))
    return dir_sizes[searchsortedfirst(dir_sizes, required_size)]
end

example = readlines("examples/07.txt")
input = readlines("inputs/07.txt")

@assert part1(example) == 95437
println(part1(input))

@assert part2(example) == 24933642
println(part2(input))
