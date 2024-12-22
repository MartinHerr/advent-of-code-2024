#!/usr/bin/env python3
from parser import parse_input

PATTERN = ["X", "M", "A", "S"]

def search_pattern(grid):
    count = 0
    extra_len = len(PATTERN) - 1
    for y, line in enumerate(grid):
        if extra_len <= y < len(grid) - extra_len:
            for x, _ in enumerate(line):
                if extra_len <= x < len(line) - extra_len:
                    if is_valid_pattern(y, x, grid):
                        print(f"y: {y}, x: {x}")
                        count += 1
    return count

def is_valid_pattern(y, x, grid, pattern="MAS"):
    if (grid[y][x] == pattern[1]):
        top_left = grid[y - 1][x - 1]
        top_right = grid[y - 1][x + 1]
        bottom_left = grid[y + 1][x - 1]
        bottom_right = grid[y + 1][x + 1]
        if ((top_left == pattern[0] and bottom_right == pattern[2]) or (top_left == pattern[2] and bottom_right == pattern[0])):
            if ((top_right == pattern[0] and bottom_left == pattern[2]) or (top_right == pattern[2] and bottom_left == pattern[0])):
                return True
    return False

if __name__ == "__main__":
    with open("input.txt") as input:
        grid = parse_input(input)
        for line in grid:
            print(line)
    print(search_pattern(grid))