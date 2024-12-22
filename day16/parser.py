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
                start = (x, y, ">")
            elif char == "E":
                end = (x, y)
    return map, maze, start, end

def count_output(ouptut):
    count = 0
    for line in output.readlines():
        line = line.strip("\n")
        for char in line:
            if char == "O":
                count += 1
    print(count)

def diff_output(input, output):
    diffs = []
    for y, line in enumerate(output.readlines()):
        line = line.strip("\n")
        for x, char in enumerate(line):
            if char != input[y][x]:
                diffs.append((x, y))
    return diffs

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        map, maze, start, end = parse_input(input)
    for line in map:
        print(line)
    with open("map_sur_input_martin.txt") as output:
        count_output(output)
        diffs = diff_output()
