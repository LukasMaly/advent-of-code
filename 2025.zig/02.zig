// Day 2: Gift Shop
// https://adventofcode.com/2025/day/2

const std = @import("std");

fn part1(path: []const u8) !u64 {
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var sum: u64 = 0;
    while (try reader.interface.takeDelimiter(',')) |line| {
        var iterator = std.mem.splitScalar(u8, line, '-');
        const a: u64 = try std.fmt.parseInt(u64, iterator.next().?, 10);
        const b: u64 = try std.fmt.parseInt(u64, iterator.next().?, 10);
        var buffer: [50]u8 = undefined;
        for (a..b + 1) |value| {
            const str = try std.fmt.bufPrint(&buffer, "{d}", .{value});
            if (str.len % 2 == 0) {
                if (std.mem.eql(u8, str[0..(str.len / 2)], str[(str.len / 2)..])) {
                    sum += value;
                }
            }
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
    while (try reader.interface.takeDelimiter(',')) |line| {
        var iterator = std.mem.splitScalar(u8, line, '-');
        const a: u64 = try std.fmt.parseInt(u64, iterator.next().?, 10);
        const b: u64 = try std.fmt.parseInt(u64, iterator.next().?, 10);
        var buffer: [50]u8 = undefined;
        for (a..b + 1) |value| {
            const str = try std.fmt.bufPrint(&buffer, "{d}", .{value});
            var invalid = false;
            for (1..(str.len / 2 + 1)) |size| {
                if (str.len % size == 0) {
                    var repeating = true;
                    for (0..(str.len / size - 1)) |i| {
                        if (std.mem.eql(u8, str[i * size .. (i + 1) * size], str[(i + 1) * size .. (i + 2) * size]) == false) {
                            repeating = false;
                            break;
                        }
                    }
                    if (repeating) {
                        invalid = true;
                        break;
                    }
                }
            }
            if (invalid) {
                sum += value;
            }
        }
    }
    return sum;
}

pub fn main() !void {
    std.debug.assert(try part1("./examples/02.txt") == 1227775554);
    std.debug.print("{d}\n", .{try part1("./inputs/02.txt")});
    std.debug.assert(try part2("./examples/02.txt") == 4174379265);
    std.debug.print("{d}\n", .{try part2("./inputs/02.txt")});
}
