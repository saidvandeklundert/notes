// zig run .\print.zig

// Importing std gives access to the print function:
const std = @import("std");
// We can alias the print function to a shorter name:
const print = std.debug.print;


pub fn main() void {
    // Print something:
    var string = "world";    
    std.debug.print("Hello, {s}!\n", .{string});

    // Print something using the alias:
    const array = [5]u8{ 'H', 'e', 'l', 'l', 'o' };
    print("{s} world!\n", .{array});
    // We can pass in multiple arguments:
    print("{s} {s}\n", .{ array, string });
    // print a number:
    const number = 42;
    print("We can also print numbers {d}\n", .{number});
    const number_ptr = &number;
    print("Print the dereferenced pointer to a number {d}\n", .{number_ptr.*});
    const Human = struct {
        age: u8,
        name: []const u8,
    };
    const jan = Human{
        .age = 7,
        .name = "Jan van de Klundert",
    };
    print("Print struct values: {s} {}\n", .{jan.name, jan.age});
}