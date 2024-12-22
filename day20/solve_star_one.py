#!/usr/bin/env python3
import numpy as np
import heapq
from parser import parse_input
from collections import defaultdict

def distance(current, neighbor):
    return 1

def manhattan(tile1, tile2):
    dx = abs(tile1.x - tile2.x)
    dy = abs(tile1.y - tile2.y)
    return dx + dy

class Tile:
    def __init__(self, position, picoseconds, parent_tile=None):
        self.x = position[0]
        self.y = position[1]
        self.picoseconds = picoseconds
        self.parent = parent_tile
    
    def __repr__(self):
        return f"({self.x}, {self.y}), ps={self.picoseconds}, parent={self.parent.get_pos()}"

    def get_pos(self):
        return (self.x, self.y)

    def next_nearest_neighbors(self, map):
        next_nearest_neighbors = []
        if self.parent is not None:
            (parent_x, parent_y) = self.parent.get_pos()
            if abs(self.x - parent_x) == 1:
                if self.y >= 2 and map[self.y - 2][self.x] == "O":
                    next_nearest_neighbors.append((self.x, self.y - 2))
                if self.y < len(map) - 2 and map[self.y + 2][self.x] == "O":
                    next_nearest_neighbors.append((self.x, self.y + 2))
            if self.x < len(map[0]) - 2 and self.x - parent_x == 1 and map[self.y][self.x + 2] == "O":
                    next_nearest_neighbors.append((self.x + 2, self.y))
            if self.x >= 2 and self.x - parent_x == -1 and map[self.y][self.x - 2] == "O":
                    next_nearest_neighbors.append((self.x - 2, self.y))

            if abs(self.y - parent_y) == 1:
                if self.x >= 2 and map[self.y][self.x - 2] == "O":
                    next_nearest_neighbors.append((self.x - 2, self.y))
                if self.x < len(map[0]) - 2 and map[self.y][self.x + 2] == "O":
                    next_nearest_neighbors.append((self.x + 2, self.y))
            if self.y < len(map) - 2 and self.y - parent_y == 1 and map[self.y + 2][self.x] == "O":
                    next_nearest_neighbors.append((self.x, self.y + 2))
            if self.y >= 2 and self.y - parent_y == -1 and map[self.y - 2][self.x] == "O":
                    next_nearest_neighbors.append((self.x, self.y - 2))
        return next_nearest_neighbors
    
def find_next_pos(tile, map, previous_tile=None):
    next_positions = {
        (tile.x + 1, tile.y),
        (tile.x - 1, tile.y),
        (tile.x, tile.y + 1),
        (tile.x, tile.y - 1)
    }
    if previous_tile is not None:
        next_positions.remove(previous_tile.get_pos())
    for pos in next_positions:
        if map[pos[1]][pos[0]] == ".":
            return pos
    return (-1, -1)

def build_path(map, start, end):
    cheats = {}
    # Building Start tile
    pos = start
    tiles = {}
    picoseconds = 0
    current = Tile(pos, picoseconds)
    map[pos[1]][pos[0]] = "O"
    tiles[current.get_pos()] = current
    pos = find_next_pos(current, map)
    # Building tiles
    while pos != (-1, -1):
        picoseconds += 1
        previous = current
        current = Tile(pos, picoseconds, parent_tile=previous)
        map[pos[1]][pos[0]] = "O"
        tiles[current.get_pos()] = current
        pos = find_next_pos(current, map, previous_tile=previous)
        shortcuts = [current.picoseconds - 2 - tiles[neighbor_pos].picoseconds\
                     for neighbor_pos in current.next_nearest_neighbors(map)]
        nnn = current.next_nearest_neighbors(map)
        if nnn:
            shortcuts = [current.picoseconds - 2 - tiles[neighbor_pos].picoseconds\
                         for neighbor_pos in current.next_nearest_neighbors(map)]
            for shortcut in shortcuts:
                if shortcut in cheats:
                    cheats[shortcut] += 1
                else:
                    cheats[shortcut] = 1
    # Building End tile
    pos = end
    picoseconds += 1
    previous = current
    current = Tile(pos, picoseconds, parent_tile=previous)
    tiles[current.get_pos()] = current
    nnn = current.next_nearest_neighbors(map)
    if nnn:
        shortcuts = [current.picoseconds - 2 - tiles[neighbor_pos].picoseconds\
                        for neighbor_pos in current.next_nearest_neighbors(map)]
        for shortcut in shortcuts:
            if shortcut in cheats:
                cheats[shortcut] += 1
            else:
                cheats[shortcut] = 1
    return cheats

def count_supercheats(map, start, end, threshold=100):
    count = 0
    cheats = build_path(map, start, end)
    # print(cheats)
    for cheat in cheats:
        if cheat >= threshold:
            count += cheats[cheat]
    return count

def plot_map(map):
    for line in map:
        print("".join(line))

if __name__ == "__main__":
    with open("input.txt") as input:
        map, maze, start, end = parse_input(input)
    # plot_map(map)
    # print(f"Start: {start}")
    # print(f"End: {end}")
    supercheats = count_supercheats(map, start, end)
    # plot_map(map)
    print(supercheats)