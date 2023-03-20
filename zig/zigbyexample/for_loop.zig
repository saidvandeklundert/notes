// zig run .\for_loop.zig
const std = @import("std");
const print = std.debug.print;

pub fn main() void{
    const items = [_]i32 { 4, 5, 3, 4, 0 };
    var sum: i32 = 0;

    // For loops iterate over slices and arrays.
    // first reference the slice/array, then name the var that will hold the current item
    for (items) |item| {
        // Break and continue are supported.

        sum += item;
        print("{d}\n", .{sum});

    }
    print("fin", .{});    
}