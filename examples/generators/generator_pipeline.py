"""
Pipeline of generators.
"""
import pathlib


def get_paths(topdir, pattern):
    for path in pathlib.Path(topdir).rglob(pattern):
        if path.exists():
            yield path


def get_files(paths):
    for path in paths:
        with path.open("rt") as f:
            yield f


def get_lines(files):
    for file in files:
        yield from file


def get_comments(lines):
    for line in lines:
        if "#" in line:
            yield line


def print_matching(lines, substring):
    for line in lines:
        if substring in line:
            print(line, end="")


paths = get_paths("..", "*.py")
files = get_files(paths)
lines = get_lines(files)
comments = get_comments(lines)
print_matching(comments, "the")
