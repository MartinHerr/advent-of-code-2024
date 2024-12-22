#!/usr/bin/env python3
from parser import parse_input

def place_antinode(a1, a2, size):
    x = 2 * a2[0] - a1[0]
    y = 2 * a2[1] - a1[1]
    # print(f"a1: {a1}, a2: {a2}, an: {(x, y)}")
    if 0 <= x < size[0] and 0 <= y < size[1]:
        return (x, y)
    else:
        return None

def locate_antinodes(antennas, size):
    count = 0
    antinodes = {}
    for antenna_type in antennas:
        for i, a1 in enumerate(antennas[antenna_type]):
            for j, a2 in enumerate(antennas[antenna_type]):
                if j != i:
                    antinode = place_antinode(a1, a2, size)
                    if antinode is not None:
                        (x, y) = antinode
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