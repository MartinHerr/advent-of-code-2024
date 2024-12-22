#!/usr/bin/env python3
def parse_input(input):
    map = []
    maze = {}
    for y, line in enumerate(input.readlines()):
        map.append([])
        line = line.strip("\n")
        for x, char in enumerate(line):
            map[-1].append(char)
            maze[(x, y)] = char
            if char == "S":
                start = (x, y)
            elif char == "E":
                end = (x, y)
    return map, maze, start, end

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        map, maze, start, end = parse_input(input)
    for line in map:
        print(line)
