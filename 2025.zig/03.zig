// Day 3: Lobby
// https://adventofcode.com/2025/day/3

const std = @import("std");

fn part1(path: []const u8) !u64 {
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var sum: u64 = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        var a: u8 = 0;
        var b: u8 = 0;
        var index: usize = 0;
        for (line, 0..) |c, i| {
            if (c - 48 > a) {
                a = c - 48;
                index = i;
            }
        }
        if (index == line.len - 1) {
            for (line[0..(line.len - 1)]) |c| {
                if (c - 48 > b) {
                    b = c - 48;
                }
            }
            sum += b * 10 + a;
        } else {
            for (line[index + 1 ..]) |c| {
                if (c - 48 > b) {
                    b = c - 48;
                }
            }
            sum += a * 10 + b;
        }
    }
    return sum;
}

fn part2(path: []const u8) !u64 {
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var sum: u64 = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        var joltage = std.mem.zeroes([12]u8);
        for (line, 0..) |c, i| {
            const len: i32 = @intCast(line.len);
            const pos: i32 = @intCast(i);
            for (joltage[@max(0, 12 - (len - pos))..], @max(0, 12 - (len - pos))..) |n, j| {
                if (c - 48 > n) {
                    joltage[j] = c - 48;
                    for ((j + 1)..12) |x| {
                        joltage[x] = 0;
                    }
                    break;
                }
            }
        }
        var number: usize = 0;
        for (joltage, 0..) |n, i| {
            number += std.math.pow(usize, 10, (11 - i)) * n;
        }
        sum += number;
    }
    return sum;
}

pub fn main() !void {
    std.debug.assert(try part1("./examples/03.txt") == 357);
    std.debug.print("{d}\n", .{try part1("./inputs/03.txt")});
    std.debug.assert(try part2("./examples/03.txt") == 3121910778619);
    std.debug.print("{d}\n", .{try part2("./inputs/03.txt")});
}
