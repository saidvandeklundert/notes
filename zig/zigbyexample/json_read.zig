// zig run .\json_read.zig
const std = @import("std");
const Allocator = std.mem.Allocator;

pub fn main() !void {
  var gpa = std.heap.GeneralPurposeAllocator(.{}){};
  const allocator = gpa.allocator();

  const human = try readJSON(allocator, "human.json");
  std.debug.print("Human.name: {s}\nHuman.age: {d}\n", .{human.name,human.age});
}

// Read target JSON file and return a struct of the type Human:
fn readJSON(allocator: Allocator, path: []const u8) !Human {
  const data = try std.fs.cwd().readFileAlloc(allocator, path, 512);
  defer allocator.free(data);

  var stream = std.json.TokenStream.init(data);
  return try std.json.parse(Human, &stream, .{.allocator = allocator});
}

const Human = struct {
  name: []const u8,
  age: u8
};