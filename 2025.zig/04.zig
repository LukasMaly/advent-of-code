// Day 4: Printing Department
// https://adventofcode.com/2025/day/4

const std = @import("std");

fn part1(path: []const u8) !u32 {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var sum: u32 = 0;
    var n: usize = 0;
    var m: usize = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        n += 1;
        m = line.len;
    }
    try reader.seekTo(0);
    var grid = try allocator.alloc(u8, (m + 2) * (n + 2));
    defer allocator.free(grid);
    @memset(grid, 0);
    var row: usize = 1;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        for (line, 1..) |c, col| {
            if (c == '@') {
                grid[(row * (m + 2)) + col] = 1;
            }
        }
        row += 1;
    }
    for (1..m + 1) |y| {
        for (1..n + 1) |x| {
            if (grid[(y * (m + 2)) + x] == 0) continue;
            var rolls: u8 = 0;
            for (0..3) |j| {
                for (0..3) |i| {
                    if (j == 1 and i == 1) continue;
                    rolls += grid[((y + j - 1) * (m + 2)) + x + i - 1];
                }
            }
            if (rolls < 4) {
                sum += 1;
            }
        }
    }
    return sum;
}

fn part2(path: []const u8) !u32 {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var sum: u32 = 0;
    var n: usize = 0;
    var m: usize = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        n += 1;
        m = line.len;
    }
    try reader.seekTo(0);
    var grid = try allocator.alloc(u8, (m + 2) * (n + 2));
    var removed = try allocator.alloc(u8, (m + 2) * (n + 2));
    defer allocator.free(grid);
    defer allocator.free(removed);
    @memset(grid, 0);
    var row: usize = 1;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        for (line, 1..) |c, col| {
            if (c == '@') {
                grid[(row * (m + 2)) + col] = 1;
            }
        }
        row += 1;
    }
    var previous_sum: u32 = std.math.maxInt(u32);
    while (sum != previous_sum) {
        previous_sum = sum;
        @memset(removed, 0);
        for (1..m + 1) |y| {
            for (1..n + 1) |x| {
                if (grid[(y * (m + 2)) + x] == 0) continue;
                var rolls: u8 = 0;
                for (0..3) |j| {
                    for (0..3) |i| {
                        if (j == 1 and i == 1) continue;
                        rolls += grid[((y + j - 1) * (m + 2)) + x + i - 1];
                    }
                }
                if (rolls < 4) {
                    sum += 1;
                    removed[(y * (m + 2)) + x] = 1;
                }
            }
        }
        for (1..m + 1) |y| {
            for (1..n + 1) |x| {
                if (removed[(y * (m + 2)) + x] == 1) {
                    grid[(y * (m + 2)) + x] = 0;
                }
            }
        }
    }
    return sum;
}

pub fn main() !void {
    std.debug.assert(try part1("./examples/04.txt") == 13);
    std.debug.assert(try part1("./inputs/04.txt") == 1474);
    std.debug.assert(try part2("./examples/04.txt") == 43);
    std.debug.assert(try part2("./inputs/04.txt") == 8910);
}
