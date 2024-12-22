#!/usr/bin/env python3
from parser import parse_input

PATTERN = ["X", "M", "A", "S"]
NEXT_DIRECTIONS = {
    "r": (0, 1),
    "br": (1, 1),
    "b": (1, 0),
    "bl": (1, -1),
    "l": (0, -1),
    "tl": (-1, -1),
    "t": (-1, 0),
    "tr": (-1, 1)
}

def search_pattern(grid):
    count = 0
    directions = [key for key in NEXT_DIRECTIONS]
    extra_len = len(PATTERN) - 1
    for y, line in enumerate(grid):
        if extra_len <= y < len(grid) - extra_len:
            for x, char in enumerate(line):
                if extra_len <= x < len(line) - extra_len:
                    for direction in directions:
                        if is_valid_pattern(y, x, grid, direction, PATTERN):
                            count += 1
    return count

def is_valid_pattern(y, x, grid, direction, pattern):
    if (len(pattern) == 1):
        return grid[y][x] == pattern[0]
    else:
        if grid[y][x] == pattern[0]:
            next_y = y + NEXT_DIRECTIONS[direction][0]
            next_x = x + NEXT_DIRECTIONS[direction][1]
            return is_valid_pattern(next_y, next_x, grid, direction, pattern[1:])
        else:
            return False

if __name__ == "__main__":
    with open("input.txt") as input:
        grid = parse_input(input)
    print(search_pattern(grid))