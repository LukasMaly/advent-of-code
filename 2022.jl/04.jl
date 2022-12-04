lines = readlines("inputs/04.txt")

# Part 1 & 2

fully_contains = 0
overlaps = 0

for line in lines
    m = match(r"(\d+)-(\d+),(\d+)-(\d+)", line)
    a = parse(Int, m[1])
    b = parse(Int, m[2])
    c = parse(Int, m[3])
    d = parse(Int, m[4])
    if a <= c && d <= b
        global fully_contains += 1
        global overlaps += 1
    elseif c <= a && b <= d
        global fully_contains += 1
        global overlaps += 1
    elseif a <= c && c <= b
        global overlaps += 1
    elseif a <= d && d <= b
        global overlaps += 1
    elseif c <= a && a <= d
        global overlaps += 1
    elseif c <= b && b <= d
        global overlaps += 1
    end
end

println(fully_contains)
println(overlaps)
