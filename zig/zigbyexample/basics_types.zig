// zig run .\basics_types.zig
const std = @import("std");
const print = std.debug.print;

const constant: i32 = 5;  // immutable signed 32-bit constant
var variable: u32 = 5000; // mutable unsigned 32-bit variable


// Array: [number of elements]Type:
const array = [5]u8{ 'h', 'e', 'l', 'l', 'o' };

var msg = "string literal";

pub fn main() void {
    print("Hello, {s}!\n", .{"World"});
    print("print a string: {s}\n", .{msg});

    const one_plus_one: i32 = 1 + 1;
    print("1 + 1 = {}\n", .{one_plus_one});

}