// Day 8: Playground
// https://adventofcode.com/2025/day/8

const std = @import("std");

fn part1(path: []const u8, iters: u16) !u64 {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var m: usize = 1;
    while (try reader.interface.takeDelimiter('\n')) |_| {
        m += 1;
    }
    var boxes = try allocator.alloc(u32, 3 * m);
    defer allocator.free(boxes);
    try reader.seekTo(0);
    m = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        var n: usize = 0;
        var iter = std.mem.splitSequence(u8, line, ",");
        while (iter.next()) |num| {
            boxes[m * 3 + n] = try std.fmt.parseInt(u32, num, 10);
            n += 1;
        }
        m += 1;
    }
    const Entry = struct {
        key: struct { usize, usize },
        value: u32,
    };
    var dists = std.ArrayList(Entry).empty;
    defer dists.deinit(allocator);
    for (0..m - 1) |i| {
        for (i + 1..m) |j| {
            try dists.append(allocator, .{ .key = .{ i, j }, .value = euclidean(boxes[(i * 3)..(i * 3 + 3)], boxes[(j * 3)..(j * 3 + 3)]) });
        }
    }
    std.mem.sort(Entry, dists.items, {}, struct {
        fn lessThan(_: void, a: Entry, b: Entry) bool {
            return a.value < b.value;
        }
    }.lessThan);
    var circs = std.AutoHashMap(usize, std.ArrayList(usize)).init(allocator);
    defer circs.deinit();
    var n_circs: usize = 0;
    for (0..iters) |i| {
        const min_pair = dists.items[i].key;
        var where_found: struct { usize, usize } = .{ std.math.maxInt(usize), std.math.maxInt(usize) };
        var circs_iter = circs.iterator();
        while (circs_iter.next()) |entry| {
            if (where_found[0] == std.math.maxInt(usize) and std.mem.containsAtLeastScalar(usize, entry.value_ptr.*.items, 1, min_pair[0])) {
                where_found[0] = entry.key_ptr.*;
            }
            if (where_found[1] == std.math.maxInt(usize) and std.mem.containsAtLeastScalar(usize, entry.value_ptr.*.items, 1, min_pair[1])) {
                where_found[1] = entry.key_ptr.*;
            }
        }
        if (where_found[0] != std.math.maxInt(usize) and where_found[1] == std.math.maxInt(usize)) {
            try circs.getPtr(where_found[0]).?.*.append(allocator, min_pair[1]);
        } else if (where_found[0] == std.math.maxInt(usize) and where_found[1] != std.math.maxInt(usize)) {
            try circs.getPtr(where_found[1]).?.*.append(allocator, min_pair[0]);
        } else if (where_found[0] != std.math.maxInt(usize) and where_found[1] != std.math.maxInt(usize)) {
            if (where_found[0] != where_found[1]) {
                try circs.getPtr(where_found[0]).?.*.appendSlice(allocator, circs.get(where_found[1]).?.items);
                _ = circs.remove(where_found[1]);
            }
        } else if (where_found[0] == std.math.maxInt(usize) and where_found[1] == std.math.maxInt(usize)) {
            var list = std.ArrayList(usize).empty;
            try list.append(allocator, min_pair[0]);
            try list.append(allocator, min_pair[1]);
            try circs.put(n_circs, list);
            n_circs += 1;
        }
    }
    var lengths = try allocator.alloc(usize, circs.count());
    var circs_iter = circs.iterator();
    var i: usize = 0;
    while (circs_iter.next()) |entry| {
        lengths[i] = entry.value_ptr.*.items.len;
        entry.value_ptr.deinit(allocator);
        i += 1;
    }
    std.mem.sort(usize, lengths, {}, comptime std.sort.desc(usize));
    return lengths[0] * lengths[1] * lengths[2];
}

fn part2(path: []const u8) !u64 {
    const allocator = std.heap.page_allocator;
    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();
    var file_buffer: [4096]u8 = undefined;
    var reader = file.reader(&file_buffer);
    var m: usize = 1;
    while (try reader.interface.takeDelimiter('\n')) |_| {
        m += 1;
    }
    var boxes = try allocator.alloc(u32, 3 * m);
    defer allocator.free(boxes);
    try reader.seekTo(0);
    m = 0;
    while (try reader.interface.takeDelimiter('\n')) |line| {
        var n: usize = 0;
        var iter = std.mem.splitSequence(u8, line, ",");
        while (iter.next()) |num| {
            boxes[m * 3 + n] = try std.fmt.parseInt(u32, num, 10);
            n += 1;
        }
        m += 1;
    }
    const Entry = struct {
        key: struct { usize, usize },
        value: u32,
    };
    var dists = std.ArrayList(Entry).empty;
    defer dists.deinit(allocator);
    for (0..m - 1) |i| {
        for (i + 1..m) |j| {
            try dists.append(allocator, .{ .key = .{ i, j }, .value = euclidean(boxes[(i * 3)..(i * 3 + 3)], boxes[(j * 3)..(j * 3 + 3)]) });
        }
    }
    std.mem.sort(Entry, dists.items, {}, struct {
        fn lessThan(_: void, a: Entry, b: Entry) bool {
            return a.value < b.value;
        }
    }.lessThan);
    var circs = std.AutoHashMap(usize, std.ArrayList(usize)).init(allocator);
    defer circs.deinit();
    var n_circs: usize = 0;
    var i: usize = 0;
    while (true) {
        const min_pair = dists.items[i].key;
        var where_found: struct { usize, usize } = .{ std.math.maxInt(usize), std.math.maxInt(usize) };
        var circs_iter = circs.iterator();
        while (circs_iter.next()) |entry| {
            if (where_found[0] == std.math.maxInt(usize) and std.mem.containsAtLeastScalar(usize, entry.value_ptr.*.items, 1, min_pair[0])) {
                where_found[0] = entry.key_ptr.*;
            }
            if (where_found[1] == std.math.maxInt(usize) and std.mem.containsAtLeastScalar(usize, entry.value_ptr.*.items, 1, min_pair[1])) {
                where_found[1] = entry.key_ptr.*;
            }
        }
        if (where_found[0] != std.math.maxInt(usize) and where_found[1] == std.math.maxInt(usize)) {
            try circs.getPtr(where_found[0]).?.*.append(allocator, min_pair[1]);
        } else if (where_found[0] == std.math.maxInt(usize) and where_found[1] != std.math.maxInt(usize)) {
            try circs.getPtr(where_found[1]).?.*.append(allocator, min_pair[0]);
        } else if (where_found[0] != std.math.maxInt(usize) and where_found[1] != std.math.maxInt(usize)) {
            if (where_found[0] != where_found[1]) {
                try circs.getPtr(where_found[0]).?.*.appendSlice(allocator, circs.get(where_found[1]).?.items);
                _ = circs.remove(where_found[1]);
            }
        } else if (where_found[0] == std.math.maxInt(usize) and where_found[1] == std.math.maxInt(usize)) {
            var list = std.ArrayList(usize).empty;
            try list.append(allocator, min_pair[0]);
            try list.append(allocator, min_pair[1]);
            try circs.put(n_circs, list);
            n_circs += 1;
        }
        if (circs.count() == 1) {
            circs_iter = circs.iterator();
            if (circs_iter.next().?.value_ptr.*.items.len == m) {
                return @as(u64, boxes[min_pair[0] * 3]) * @as(u64, boxes[min_pair[1] * 3]);
            }
        }
        i += 1;
    }
    return 0;
}

fn euclidean(a: []u32, b: []u32) u32 {
    return std.math.sqrt(std.math.pow(u64, @max(a[0], b[0]) - @min(a[0], b[0]), 2) + std.math.pow(u64, @max(a[1], b[1]) - @min(a[1], b[1]), 2) + std.math.pow(u64, @max(a[2], b[2]) - @min(a[2], b[2]), 2));
}

pub fn main() !void {
    std.debug.assert(try part1("./examples/08.txt", 10) == 40);
    std.debug.assert(try part1("./inputs/08.txt", 1000) == 352584);
    std.debug.assert(try part2("./examples/08.txt") == 25272);
    std.debug.assert(try part2("./inputs/08.txt") == 9617397716);
}
