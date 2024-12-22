#!/usr/bin/env python3
from collections import defaultdict

def parse_input(input, size=70, bytes=1024):
    map = []
    maze = defaultdict(lambda: ".")
    count = 0
    for y in range(size + 3):
        if y == 0 or y == size + 2:
            map.append(["#" for _ in range(size + 3)])
            for x in range(size + 3):
                maze[(x, y)] = "#"
        else:
            map.append(["#"] + ["." for _ in range(size + 1)] + ["#"])
            maze[(0, y)] = "#"
            maze[(size + 2, y)] = "#"
    for line in input.readlines():
        count += 1
        line = line.strip("\n")
        coords = [int(i) for i in line.split(",")]
        x = coords[0]
        y = coords[1]
        map[y + 1][x + 1] = "#"
        maze[(x + 1, y + 1)] = "#"
        if count >= bytes:
            break
    return map, maze, coords

def plot_map(map):
    for line in map:
        print("".join(line))

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        map, maze = parse_input(input, size=6, bytes=12)
    plot_map(map)
    print(maze)
