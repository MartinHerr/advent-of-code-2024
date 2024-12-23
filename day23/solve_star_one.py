#!/usr/bin/env python3
from parser import parse_input

def find_triangles(graph):
    # Works with un-directed graph. Parser should add links in both directions
    triangles = set()
    for node, neighbors in graph.items():
        for i, neighbor1 in enumerate(neighbors):
            for neighbor2 in neighbors[i + 1:]:
                if neighbor2 in graph.get(neighbor1, []):
                    triangle = tuple(sorted([node, neighbor1, neighbor2]))
                    triangles.add(triangle)
    return triangles

def find_t_groups(triangles):
    count = 0
    for triangle in triangles:
        if triangle[0][0] == "t" or triangle[1][0] == "t" or triangle[2][0] == "t":
            count += 1
    return count

if __name__ == "__main__":
    with open("input.txt") as input:
        seen_computers, links = parse_input(input)
    triangles = find_triangles(links)
    count = find_t_groups(triangles)
    print(count)