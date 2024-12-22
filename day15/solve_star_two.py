#!/usr/bin/env python3
import numpy as np
import math
from parser import parse_big_map, parse_moves

def sort_by_x(box):
    return 100 * box[0] + box[1]

def sort_by_y(box):
    return 100 * box[1] + box[0]

def sum_of_boxes_gps_coordinates(map):
    result = 0
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == "[":
                result += sort_by_y((x, y))
    return result

def flip_element(position, map):
    element = map[position[1]][position[0]]
    if element == "[":
        map[position[1]][position[0]] = "]"
    elif element == "]":
        map[position[1]][position[0]] = "["

def vertical_move(visited, map, dir):
    sorted_visited = sorted(visited, key=sort_by_y)
    if dir == "^":
        for pos in sorted_visited:
            map[pos[1] - 1][pos[0]] = map[pos[1]][pos[0]]
            map[pos[1]][pos[0]] = "."
    elif dir == "v":
        for pos in sorted_visited[::-1]:
            map[pos[1] + 1][pos[0]] = map[pos[1]][pos[0]]
            map[pos[1]][pos[0]] = "."

def vertical_dfs(position, map, dir, visited):
    # visited: set of visited positions
    # position: tuple of coordinates
    if position in visited:
        return True
    element = map[position[1]][position[0]]
    if element == "#":
        return False
    elif element == ".":
        return True
    else:
        visited.add(position)
        if dir == "^":
            if element == "[":
                return vertical_dfs((position[0], position[1] - 1), map, dir, visited) and\
                    vertical_dfs((position[0] + 1, position[1]), map, dir, visited)
            if element == "]":
                return vertical_dfs((position[0], position[1] - 1), map, dir, visited) and\
                    vertical_dfs((position[0] - 1, position[1]), map, dir, visited)
        elif dir == "v":
            if element == "[":
                return vertical_dfs((position[0], position[1] + 1), map, dir, visited) and\
                    vertical_dfs((position[0] + 1, position[1]), map, dir, visited)
            if element == "]":
                return vertical_dfs((position[0], position[1] + 1), map, dir, visited) and\
                    vertical_dfs((position[0] - 1, position[1]), map, dir, visited)

def move_boxes(robot, map, dir):
    next_element_pos = robot[:]
    half_box_count = 0
    next_elements_positions = []
    if dir == "<":
        while True:
            next_element_pos[0] -= 1
            next_element = map[next_element_pos[1]][next_element_pos[0]]
            if next_element in ["[", "]"]:
                half_box_count += 1
                next_elements_positions.append(next_element_pos[:])
            elif next_element == "#":
                return
            elif next_element == ".":
                map[robot[1]][robot[0]] = "."
                robot[0] -= 1
                # print(f"Flipping at positions {next_elements_positions}")
                for pos in next_elements_positions:
                    flip_element(pos, map)
                map[robot[1]][robot[0] - half_box_count] = "["
                map[robot[1]][robot[0]] = "@"
                return
    if dir == ">":
        while True:
            next_element_pos[0] += 1
            next_element = map[next_element_pos[1]][next_element_pos[0]]
            if next_element in ["[", "]"]:
                half_box_count += 1
                next_elements_positions.append(next_element_pos[:])
            elif next_element == "#":
                return
            elif next_element == ".":
                map[robot[1]][robot[0]] = "."
                robot[0] += 1
                # print(f"Flipping at positions {next_elements_positions}")
                for pos in next_elements_positions:
                    flip_element(pos, map)
                map[robot[1]][robot[0] + half_box_count] = "]"
                map[robot[1]][robot[0]] = "@"
                return
    if dir == "^":
        next_element_pos[1] -= 1
        visited = set()
        if vertical_dfs(tuple(next_element_pos), map, dir, visited):
            # print("Boxes can be moved up!")
            # print(f"Positions visited: {sorted(visited, key=sort_by_y)}")
            vertical_move(visited, map, dir)
            map[robot[1]][robot[0]] = "."
            robot[1] -= 1
            map[robot[1]][robot[0]] = "@"
        return
    if dir == "v":
        next_element_pos[1] += 1
        visited = set()
        if vertical_dfs(tuple(next_element_pos), map, dir, visited):
            # print("Boxes can be moved down!")
            # print(f"Positions visited: {sorted(visited, key=sort_by_y)}")
            vertical_move(visited, map, dir)
            map[robot[1]][robot[0]] = "."
            robot[1] += 1
            map[robot[1]][robot[0]] = "@"
        return

def plot_map(map):
    for line in map:
        print("".join(line))

if __name__ == "__main__":
    with open("map.txt") as input:
        map, robot = parse_big_map(input)
    with open("movements.txt") as input:
        moves = [char for char in parse_moves(input)]
    # plot_map(map)
    # print(f"robot: {robot}")
    for dir in moves:
        # print(f"Move: {dir}")
        move_boxes(robot, map, dir)
    # plot_map(map)
    print(sum_of_boxes_gps_coordinates(map))
