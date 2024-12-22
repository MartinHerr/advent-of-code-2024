#!/usr/bin/env python3
import numpy as np
import heapq
from parser import parse_input
from collections import defaultdict

def print_path(path, map):
    for node in path:
        (x, y, dir) = node
        map[y][x] = dir

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def neighbors(node, maze):
    (x, y, dir) = node
    next_neighbors = []
    if dir == ">":
        next_neighbors = [(x, y, "^"), (x, y, "v")]
        if maze[(x + 1, y)] != "#":
            next_neighbors.append((x + 1, y, ">"))
    if dir == "<":
        next_neighbors = [(x, y, "^"), (x, y, "v")]
        if maze[(x - 1, y)] != "#":
            next_neighbors.append((x - 1, y, "<"))
    if dir == "^":
        next_neighbors = [(x, y, "<"), (x, y, ">")]
        if maze[(x, y - 1)] != "#":
            next_neighbors.append((x, y - 1, "^"))
    if dir == "v":
        next_neighbors = [(x, y, "<"), (x, y, ">")]
        if maze[(x, y + 1)] != "#":
            next_neighbors.append((x, y + 1, "v"))
    return next_neighbors[::-1]

def distance(current, neighbor):
    if current[2] == neighbor[2]:
        return 1
    else:
        return 1000
    
def next_free_tiles(node, maze):
    count = 0
    (x, y, dir) = node
    if dir == ">":
        i = node[0] + 1
        while True:
            if maze[(i, y)] == "#":
                break
            else:
                count += 1
                i += 1
    if dir == "<":
        i = node[0] - 1
        while True:
            if maze[(i, y)] == "#":
                break
            else:
                count += 1
                i -= 1
    if dir == "v":
        i = node[1] + 1
        while True:
            if maze[(x, i)] == "#":
                break
            else:
                count += 1
                i += 1
    if dir == "^":
        i = node[1] - 1
        while True:
            if maze[(x, i)] == "#":
                break
            else:
                count += 1
                i -= 1
    return count

def h(node, goal, maze):
    dx = abs(node[0] - goal[0])
    dy = abs(node[1] - goal[1])
    rotation_cost = 1000 if (node[2] == ">" and node[0] > goal[0]) or \
                           (node[2] == "<" and node[0] < goal[0]) or \
                           (node[2] == "^" and node[1] < goal[1]) or \
                           (node[2] == "v" and node[1] > goal[1]) else 0
    return dx + dy + rotation_cost

def custom_h(node, goal, maze):
    # Custom h function that gives a min distance heuristic, based on
    # the min number of rotations required to reach the goal without any walls 
    dx, dy = abs(goal[0] - node[0]), abs(goal[1] - node[1])
    facing = node[2]
    # Aligned case
    if (facing == ">" and node[1] == goal[1]) or (facing == "<" and node[1] == goal[1]):
        return dx + dy if node[0] <= goal[0] else 2000 + dx + dy
    if (facing == "v" and node[0] == goal[0]) or (facing == "^" and node[0] == goal[0]):
        return dx + dy if node[1] <= goal[1] else 2000 + dx + dy
    # Goal in front of node
    if (facing == ">" and node[0] <= goal[0]) or (facing == "<" and node[0] >= goal[0]) or \
       (facing == "v" and node[1] <= goal[1]) or (facing == "^" and node[1] >= goal[1]):
        return 1000 + dx + dy
    # Goal behind node
    return 2000 + dx + dy

def A_star(start, goal, h, maze):
    came_from = {}
    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0
    f_score = defaultdict(lambda: float("inf"))
    f_score[start] = h(start, goal, maze)
    open_set = []
    heapq.heappush(open_set, (f_score[start], start))
    while open_set:
        current = heapq.heappop(open_set)[1]
        if (current[0], current[1]) == goal:
            return reconstruct_path(came_from, current)
        for neighbor in neighbors(current, maze):
            tentative_g_score = g_score[current] + distance(current, neighbor)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor, goal, maze)
                if neighbor not in open_set:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return -1

def score(path):
    result = 0
    for i, node in enumerate(path):
        if i == 0:
            (prev_x, prev_y, prev_dir) = node
        else:
            (x, y, dir) = node
            if dir == prev_dir:
                result += 1
            else:
                result += 1000
            (prev_x, prev_y, prev_dir) = node
    return result

def plot_map(map):
    for line in map:
        print("".join(line))

if __name__ == "__main__":
    with open("input.txt") as input:
        map, maze, start, goal = parse_input(input)
    # plot_map(map)
    print(f"Start: {start}")
    print(f"End: {goal}")
    path = A_star(start, goal, h, maze)
    # print_path(path, map)
    # plot_map(map)
    print(score(path))