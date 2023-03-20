// zig run .\print_the_type.zig
const std = @import("std");
const print = std.debug.print;

pub fn main() void {
    
    var string = "world";    
    const T1 = @TypeOf(string);

    print("string is of the type {}\n", .{T1});
    const Human = struct {
        age: u8,
        name: []const u8,
    };
    const jan = Human{
        .age = 7,
        .name = "Jan van de Klundert",
    };    
    const T2 = @TypeOf(jan);

    print("jan is of the type {}\n", .{T2});   
    const jan_ptr = &jan; 
    const T3 = @TypeOf(jan_ptr);

    print("jan_ptr is of the type {}\n", .{T3});

    debugValue(string);
    debugStruct(jan);     
    
}


fn debugValue(data: anytype) void {
    const T = @TypeOf(data);
    print("{}\n", .{T});
}

fn debugStruct(data: anytype) void {
    const T = @TypeOf(data);
    print("{}\n", .{T});
    inline for (@typeInfo(T).Struct.fields) | field|{
        std.debug.print("{any}\n",.{@field(data, field.name)});
    }
}