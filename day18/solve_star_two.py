#!/usr/bin/env python3
import numpy as np
import heapq
from parser import parse_input
from collections import defaultdict

def print_path(path, map):
    for node in path:
        (x, y, dir) = node
        if map[y][x] != "#":
            map[y][x] = "O"

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
        if maze[(x + 1, y)] != "#":
            next_neighbors.append((x + 1, y, ">"))
        if maze[(x, y - 1)] != "#":
            next_neighbors.append((x, y - 1, "^"))
        if maze[(x, y + 1)] != "#":
            next_neighbors.append((x, y + 1, "v"))
    if dir == "<":
        if maze[(x - 1, y)] != "#":
            next_neighbors.append((x - 1, y, "<"))
        if maze[(x, y - 1)] != "#":
            next_neighbors.append((x, y - 1, "^"))
        if maze[(x, y + 1)] != "#":
            next_neighbors.append((x, y + 1, "v"))
    if dir == "^":
        if maze[(x, y - 1)] != "#":
            next_neighbors.append((x, y - 1, "^"))
        if maze[(x - 1, y)] != "#":
            next_neighbors.append((x - 1, y, "<"))
        if maze[(x + 1, y)] != "#":
            next_neighbors.append((x + 1, y, ">"))
    if dir == "v":
        if maze[(x, y + 1)] != "#":
            next_neighbors.append((x, y + 1, "v"))
        if maze[(x - 1, y)] != "#":
            next_neighbors.append((x - 1, y, "<"))
        if maze[(x + 1, y)] != "#":
            next_neighbors.append((x + 1, y, ">"))
    return next_neighbors

def distance(current, neighbor):
    return 1

def h(node, goal, maze):
    dx = abs(node[0] - goal[0])
    dy = abs(node[1] - goal[1])
    return dx + dy

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
                # print(f"Detected shortest distance {distance(current, neighbor)} between {current} and {neighbor}")
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor, goal, maze)
                if neighbor not in open_set:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return -1

def score(path):
    return len(path) - 1

def plot_map(map):
    for line in map:
        print("".join(line))

def search_blocking_byte(start, goal, input, first=1024, last=3450):
    bytes = first
    while True:
        print(f"Searching path for byte {bytes}")
        with open("input.txt") as input:
            map, maze, last = parse_input(input, size=70, bytes=bytes)
        path = A_star(start, goal, h, maze)
        if path == -1:
            break
        bytes += 1
    return last


if __name__ == "__main__":
    start = (1, 1, "v")
    goal = (71, 71)
    print(search_blocking_byte(start, goal, input))