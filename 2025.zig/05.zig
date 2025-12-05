// Day 5: Cafeteria
// https://adventofcode.com/2025/day/5

const std = @import("std");

fn part1(path: []const u8) !u64 {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var sum: u64 = 0;
    var n: usize = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        if (line.len == 0) {
            break;
        }
        n += 1;
    }
    var fresh_ids = try allocator.alloc(u64, n * 2);
    defer allocator.free(fresh_ids);
    n = 0;
    try reader.seekTo(0);
    while (try reader.interface.takeDelimiter('\n')) |line| {
        if (line.len == 0) {
            break;
        }
        var iter = std.mem.splitScalar(u8, line, '-');
        while (iter.next()) |x| {
            fresh_ids[n] = try std.fmt.parseInt(u64, x, 10);
            n += 1;
        }
    }
    while (try reader.interface.takeDelimiter('\n')) |line| {
        const id = try std.fmt.parseInt(u64, line, 10);
        var is_fresh = false;
        for (0..(n / 2)) |i| {
            if (fresh_ids[2 * i] <= id and id <= fresh_ids[2 * i + 1]) {
                is_fresh = true;
                break;
            }
        }
        if (is_fresh == true) {
            sum += 1;
        }
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
    var n: usize = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        if (line.len == 0) {
            break;
        }
        n += 1;
    }
    var los = try allocator.alloc(u64, n);
    var his = try allocator.alloc(u64, n);
    defer allocator.free(los);
    defer allocator.free(his);
    n = 0;
    try reader.seekTo(0);
    while (try reader.interface.takeDelimiter('\n')) |line| {
        if (line.len == 0) {
            break;
        }
        var iter = std.mem.splitScalar(u8, line, '-');
        los[n] = try std.fmt.parseInt(u64, iter.next().?, 10);
        his[n] = try std.fmt.parseInt(u64, iter.next().?, 10) + 1;
        n += 1;
    }
    std.mem.sort(u64, his, los, struct {
        fn lessThan(_: []u64, a: usize, b: usize) bool {
            return a < b;
        }
    }.lessThan);
    std.mem.sort(u64, los, {}, std.sort.asc(u64));
    var cur_lo: u64 = los[0];
    var cur_hi: u64 = his[0];
    for (los[1..], his[1..]) |lo, hi| {
        if (cur_hi < lo) {
            sum += cur_hi - cur_lo;
            cur_lo = lo;
            cur_hi = hi;
        } else if (cur_hi < hi) {
            cur_hi = hi;
        }
    }
    sum += cur_hi - cur_lo;
    return sum;
}

pub fn main() !void {
    std.debug.assert(try part1("./examples/05.txt") == 3);
    std.debug.assert(try part1("./inputs/05.txt") == 517);
    std.debug.assert(try part2("./examples/05.txt") == 14);
    std.debug.assert(try part2("./inputs/05.txt") == 336173027056994);
}
