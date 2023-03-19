// zig run .\for_loop.zig
const std = @import("std");
const print = std.debug.print;

pub fn main() void{
    const array_items = [_]i32 { 4, 5, 3, 4, 0 };
    var sum: i32 = 0;

    // For loops iterate over slices and arrays.
    for (array_items) |value| {
        // Break and continue are supported.
        if (value == 0) {
            continue;
        }
        sum += value;
        print("{d}\n", .{sum});

    }
    print("fin", .{});    
}