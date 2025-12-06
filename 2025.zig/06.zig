// Day 6: Trash Compactor
// https://adventofcode.com/2025/day/6

const std = @import("std");

fn part1(path: []const u8) !u64 {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var sum: u64 = 0;
    var m: usize = 0;
    var n: usize = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        var iter = std.mem.splitSequence(u8, line, " ");
        while (iter.next()) |num| {
            if (std.mem.eql(u8, num, "")) continue;
            if (m == 0) {
                n += 1;
            }
        }
        m += 1;
    }
    var nums = try allocator.alloc(u16, (m - 1) * n);
    defer allocator.free(nums);
    var row: usize = 0;
    try reader.seekTo(0);
    while (try reader.interface.takeDelimiter('\n')) |line| {
        if (row == m - 1) {
            var iter = std.mem.splitSequence(u8, line, " ");
            var col: usize = 0;
            while (iter.next()) |num| {
                if (std.mem.eql(u8, num, "")) continue;
                var res: u64 = 0;
                if (std.mem.eql(u8, num, "*")) {
                    res = 1;
                    for (0..m - 1) |i| {
                        res *= nums[(i * n) + col];
                    }
                } else { // if (std.mem.eql(u8, num, "+")) {
                    for (0..m - 1) |i| {
                        res += nums[(i * n) + col];
                    }
                }
                sum += res;
                col += 1;
            }
        } else {
            var iter = std.mem.splitSequence(u8, line, " ");
            var col: usize = 0;
            while (iter.next()) |num| {
                if (std.mem.eql(u8, num, "")) continue;
                nums[(row * n) + col] = try std.fmt.parseInt(u16, num, 10);
                col += 1;
            }
        }
        row += 1;
    }
    return sum;
}

fn part2(path: []const u8) !u64 {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var sum: u64 = 0;
    var m: usize = 0;
    var n: usize = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        var iter = std.mem.splitSequence(u8, line, " ");
        while (iter.next()) |num| {
            if (std.mem.eql(u8, num, "")) continue;
            if (m == 0) {
                n += 1;
            }
        }
        m += 1;
    }
    var widths = try allocator.alloc(u16, n);
    defer allocator.free(widths);
    var row: usize = 0;
    var len: usize = 0;
    var opers = try allocator.alloc(u8, n);
    try reader.seekTo(0);
    while (try reader.interface.takeDelimiter('\n')) |line| {
        len = line.len;
        if (row == m - 1) {
            var col: usize = 0;
            var width: u8 = 0;
            var iter = std.mem.splitSequence(u8, line, " ");
            opers[col] = line[0];
            while (iter.next()) |num| {
                if (std.mem.eql(u8, num, "+") or std.mem.eql(u8, num, "*")) {
                    if (width > 0) {
                        opers[col + 1] = num[0];
                        widths[col] = width + 1;
                        width = 0;
                        col += 1;
                    }
                } else {
                    width += 1;
                }
                widths[col] = width + 1;
            }
        }
        row += 1;
    }
    var lines = try allocator.alloc(u8, (m - 1) * len);
    defer allocator.free(lines);
    row = 0;
    try reader.seekTo(0);
    while (try reader.interface.takeDelimiter('\n')) |line| {
        if (row < m - 1) {
            @memcpy(lines[(row * len)..((row + 1) * len)], line);
            row += 1;
        }
    }
    var offset: u16 = 0;
    var num_array = try allocator.alloc(u8, m - 1);
    defer allocator.free(num_array);
    @memset(num_array, ' ');
    for (widths, 0..) |width, i| {
        var res: u64 = 0;
        if (opers[i] == '*') res = 1;
        for (0..width) |c| {
            var nonempty: u8 = 0;
            for (0..m - 1) |r| {
                if (lines[(r * len) + offset + c] != ' ') {
                    num_array[nonempty] = lines[(r * len) + offset + c];
                    nonempty += 1;
                }
            }
            var number: u32 = 0;
            if (std.mem.containsAtLeastScalar(u8, num_array, 1, ' ')) {
                number = try std.fmt.parseInt(u32, num_array[0..std.mem.indexOfScalar(u8, num_array, ' ').?], 10);
            } else {
                number = try std.fmt.parseInt(u32, num_array, 10);
            }
            if (opers[i] == '*') {
                res *= number;
            } else { // if (opers[i] == '*') {
                res += number;
            }
            @memset(num_array, ' ');
        }
        sum += res;
        offset += width + 1;
    }
    return sum;
}

pub fn main() !void {
    std.debug.assert(try part1("./examples/06.txt") == 4277556);
    std.debug.assert(try part1("./inputs/06.txt") == 6171290547579);
    std.debug.assert(try part2("./examples/06.txt") == 3263827);
    std.debug.assert(try part2("./inputs/06.txt") == 8811937976367);
}
