"""
Day 10: Cathode-Ray Tube
https://adventofcode.com/2022/day/10
"""

function parse_cycles(lines)
    instructions = Vector{Int}()
    push!(instructions, 0)
    push!(instructions, 1)
    for line in lines
        if line == "noop"
            push!(instructions, 0)
        else
            push!(instructions, parse(Int, split(line)[2]))
            push!(instructions, 0)
        end
    end
    return cumsum(instructions)
end

function part1(lines)
    cycles = parse_cycles(lines)
    indexes = [20, 60, 100, 140, 180, 220]
    return sum(cycles[indexes] .* indexes)
end

function part2(lines)
    cycles = parse_cycles(lines)
    display_width = 40
    display_height = 6
    pixels = Vector{Bool}()
    for i in range(1, length(cycles[1:(display_width * display_height)]))
        if i - 1 <= cycles[i] + ((i - 1) ÷ display_width) * display_width + 1 <= i + 1
            push!(pixels, true)
        else
            push!(pixels, false)
        end
    end
    image = ""
    for (i, pixel) in enumerate(pixels)
        image *= pixel ? "#" : "."
        if mod(i, display_width) == 0
            image *= '\n'
        end
    end
    return image
end

example = readlines("examples/10.txt")
input = readlines("inputs/10.txt")

@assert part1(example) == 13140
println(part1(input))

@assert part2(example) == """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
println(part2(input))
