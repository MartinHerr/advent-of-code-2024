#!/usr/bin/env python3
import numpy as np
import math
from parser import parse_map, parse_moves

def order_walls_along_x_and_y(walls):
    return sorted(walls, key=sort_by_x), sorted(walls, key=sort_by_y)

def sort_by_x(box):
    return 100 * box[0] + box[1]

def sort_by_y(box):
    return 100 * box[1] + box[0]

def sum_of_boxes_gps_coordinates(map):
    result = 0
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == "O":
                result += sort_by_y((x, y))
    return result

def move_boxes(robot, map, dir):
    next_element_pos = robot[:]
    box_count = 0
    if dir == "<":
        while True:
            next_element_pos[0] -= 1
            next_element = map[next_element_pos[1]][next_element_pos[0]]
            if next_element == "O":
                box_count += 1
            elif next_element == "#":
                return
            elif next_element == ".":
                map[robot[1]][robot[0]] = "."
                robot[0] -= 1
                map[robot[1]][robot[0] - box_count] = "O"
                map[robot[1]][robot[0]] = "@"
                return
    if dir == ">":
        while True:
            next_element_pos[0] += 1
            next_element = map[next_element_pos[1]][next_element_pos[0]]
            if next_element == "O":
                box_count += 1
            elif next_element == "#":
                return
            elif next_element == ".":
                map[robot[1]][robot[0]] = "."
                robot[0] += 1
                map[robot[1]][robot[0] + box_count] = "O"
                map[robot[1]][robot[0]] = "@"
                return
    if dir == "^":
        while True:
            next_element_pos[1] -= 1
            next_element = map[next_element_pos[1]][next_element_pos[0]]
            if next_element == "O":
                box_count += 1
            elif next_element == "#":
                return
            elif next_element == ".":
                map[robot[1]][robot[0]] = "."
                robot[1] -= 1
                map[robot[1] - box_count][robot[0]] = "O"
                map[robot[1]][robot[0]] = "@"
                return
    if dir == "v":
        while True:
            next_element_pos[1] += 1
            next_element = map[next_element_pos[1]][next_element_pos[0]]
            if next_element == "O":
                box_count += 1
            elif next_element == "#":
                return
            elif next_element == ".":
                map[robot[1]][robot[0]] = "."
                robot[1] += 1
                map[robot[1] + box_count][robot[0]] = "O"
                map[robot[1]][robot[0]] = "@"
                return

def plot_map(map):
    for line in map:
        print("".join(line))

if __name__ == "__main__":
    with open("map.txt") as input:
        map, walls, boxes, robot = parse_map(input)
    with open("movements.txt") as input:
        moves = [char for char in parse_moves(input)]
    print(moves)
    plot_map(map)
    print(f"robot: {robot}")
    for dir in moves:
        move_boxes(robot, map, dir)
    plot_map(map)
    print(sum_of_boxes_gps_coordinates(map))
