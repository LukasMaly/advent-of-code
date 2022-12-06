lines = readlines("inputs/06.txt")

function detect_marker(line, size)
    for i in 1:(length(line) - size + 1)
        if length(Set(line[i:(i + size - 1)])) == size
            return i + size - 1
        end
    end
end

println(detect_marker(lines[1], 4))
println(detect_marker(lines[1], 14))
