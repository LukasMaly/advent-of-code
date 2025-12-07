// Day 7: Laboratories
// https://adventofcode.com/2025/day/7

const std = @import("std");

fn part1(path: []const u8) !u64 {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var m: usize = 0;
    var n: usize = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        if (m == 0) {
            n = line.len;
        }
        m += 1;
    }
    var diagram = try allocator.alloc(u8, m * n);
    defer allocator.free(diagram);
    try reader.seekTo(0);
    m = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        @memcpy(diagram[(m * n)..((m + 1) * n)], line);
        m += 1;
    }
    const x = std.mem.indexOfScalar(u8, diagram[0..n], 'S').?;
    return beam(x, 0, m, n, diagram);
}

fn beam(x: usize, y: usize, m: usize, n: usize, diagram: []u8) u16 {
    var splits: u16 = 0;
    diagram[(y * n) + x] = '|';
    for ((y + 1)..m) |r| {
        if (diagram[(r * n) + x] == '.') {
            diagram[(r * n) + x] = '|';
        } else if (diagram[(r * n) + x] == '^') {
            if ((diagram[(r * n) + x - 1] != '|') or (diagram[(r * n) + x + 1] != '|')) {
                splits += 1;
            }
            if (diagram[(r * n) + x - 1] != '|') {
                splits += beam(x - 1, r, m, n, diagram);
            }
            if (diagram[(r * n) + x + 1] != '|') {
                splits += beam(x + 1, r, m, n, diagram);
            }
            break;
        }
    }
    return splits;
}

fn part2(path: []const u8) !u64 {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var m: usize = 0;
    var n: usize = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        if (m == 0) {
            n = line.len;
        }
        m += 1;
    }
    var diagram = try allocator.alloc(u8, m * n);
    var counts = try allocator.alloc(u64, m * n);
    defer allocator.free(diagram);
    defer allocator.free(counts);
    @memset(counts, 0);
    try reader.seekTo(0);
    m = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        @memcpy(diagram[(m * n)..((m + 1) * n)], line);
        m += 1;
    }
    counts[std.mem.indexOfScalar(u8, diagram[0..n], 'S').?] = 1;
    for (1..m) |y| {
        for (0..n) |x| {
            if (diagram[(y * n) + x] == '^') {
                counts[(y * n) + x - 1] += counts[((y - 1) * n) + x];
                counts[(y * n) + x + 1] += counts[((y - 1) * n) + x];
            } else {
                counts[(y * n) + x] += counts[((y - 1) * n) + x];
            }
        }
    }
    var sum: u64 = 0;
    for (0..n) |x| {
        sum += counts[((m - 1) * n) + x];
    }
    return sum;
}

pub fn main() !void {
    std.debug.assert(try part1("./examples/07.txt") == 21);
    std.debug.assert(try part1("./inputs/07.txt") == 1619);
    std.debug.assert(try part2("./examples/07.txt") == 40);
    std.debug.assert(try part2("./inputs/07.txt") == 23607984027985);
}
