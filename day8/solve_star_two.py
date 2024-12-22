#!/usr/bin/env python3
from parser import parse_input
from math import gcd

def find_antinodes(a1, a2, size):
    antinodes = []
    dx = a2[0] - a1[0]
    dy = a2[1] - a1[1]
    g = gcd(dx, dy)
    dir_vector = (dx // g, dy // g)
    # print(f"a1: {a1}, a2: {a2}, an: {(x, y)}")
    antinode = a1
    while 0 <= antinode[0] < size[0] and 0 <= antinode[1] < size[1]:
        antinodes.append(antinode)
        antinode = (antinode[0] + dir_vector[0], antinode[1] + dir_vector[1])
    antinode = a1
    while 0 <= antinode[0] < size[0] and 0 <= antinode[1] < size[1]:
        if antinode != a1:
            antinodes.append(antinode)
        antinode = (antinode[0] - dir_vector[0], antinode[1] - dir_vector[1])
    return antinodes

def locate_antinodes(antennas, size):
    count = 0
    antinodes = {}
    for antenna_type in antennas:
        for i, a1 in enumerate(antennas[antenna_type]):
            for a2 in antennas[antenna_type][i + 1:]:
                current_antinodes = find_antinodes(a1, a2, size)
                if len(current_antinodes) > 0:
                    for (x, y) in current_antinodes:
                        if x in antinodes:
                            if y in antinodes[x]:
                                pass
                            else:
                                antinodes[x].append(y)
                                count += 1
                        else:
                            antinodes[x] = [y]
                            count += 1
    return count

if __name__ == "__main__":
    with open("input.txt") as input:
        antennas, size = parse_input(input)
    # print(antennas)
    # print(size)
    print(locate_antinodes(antennas, size))