// Day 1: Secret Entrance
// https://adventofcode.com/2025/day/1

const std = @import("std");

fn part1(path: []const u8) !u32 {
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var dial: i32 = 50;
    var at_zero: u32 = 0;
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    while (try reader.interface.takeDelimiter('\n')) |line| {
        const number = try std.fmt.parseInt(i32, line[1..], 10);
        if (line[0] == 'L') {
            dial -= number;
        } else {
            dial += number;
        }
        if (@rem(dial, 100) == 0) {
            at_zero += 1;
        }
    }
    return at_zero;
}

fn part2(path: []const u8) !u32 {
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var dial: i32 = 50;
    var at_zero: u32 = 0;
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    while (try reader.interface.takeDelimiter('\n')) |line| {
        const number = try std.fmt.parseInt(u32, line[1..], 10);
        if (line[0] == 'L') {
            for (0..number) |_| {
                dial -= 1;
                if (@rem(dial, 100) == 0) {
                    at_zero += 1;
                }
            }
        } else {
            for (0..number) |_| {
                dial += 1;
                if (@rem(dial, 100) == 0) {
                    at_zero += 1;
                }
            }
        }
    }
    return at_zero;
}

pub fn main() !void {
    std.debug.assert(try part1("./examples/01.txt") == 3);
    std.debug.assert(try part1("./inputs/01.txt") == 1031);
    std.debug.assert(try part2("./examples/01.txt") == 6);
    std.debug.assert(try part2("./inputs/01.txt") == 5831);
}
