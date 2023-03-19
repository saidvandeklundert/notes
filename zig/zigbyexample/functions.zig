// zig run .\functions.zig
const std = @import("std");

// A function that takes 2 integers and returns their sum as an integer:
fn AddNumbers(a:i32, b:i31) i32 {
    return a + b;
}

pub fn main() void {

    const result = AddNumbers(1, 2);
    std.debug.print("{d}\n", .{result});

}