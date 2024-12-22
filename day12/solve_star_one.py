#!/usr/bin/env python3
from parser import parse_input

def populate_fences(map, horizontal_fences, vertical_fences):
    (map_y, map_x) = (len(map), len(map[0]))
    for y, line in enumerate(map):
        for x, _ in enumerate(line):
            if x < map_x - 1 and map[y][x] != map[y][x + 1]:
                vertical_fences[y][ x + 1] = 1
            if y < map_y - 1 and map[y][x] != map[y + 1][x]:
                horizontal_fences[y + 1][x] = 1
    return horizontal_fences, vertical_fences

def dfs(start_pos, map, visited, horizontal_fences, vertical_fences):
    (x, y) = start_pos
    # (map_y, map_x) = (len(map), len(map[0]))
    count = 1
    fences = 0
    visited[y][x] = 1
    # Search right
    if vertical_fences[y][x + 1]:
        fences += 1
    elif not visited[y][x + 1]:
        next_count, next_fences = dfs((x + 1, y), map, visited, horizontal_fences, vertical_fences)
        count += next_count
        fences += next_fences
    # Search down
    if horizontal_fences[y + 1][x]:
        fences += 1
    elif not visited[y + 1][x]:
        next_count, next_fences = dfs((x, y + 1), map, visited, horizontal_fences, vertical_fences)
        count += next_count
        fences += next_fences
    # Search left
    if vertical_fences[y][x]:
        fences += 1
    elif not visited[y][x - 1]:
        next_count, next_fences = dfs((x - 1, y), map, visited, horizontal_fences, vertical_fences)
        count += next_count
        fences += next_fences
    # Search up
    if horizontal_fences[y][x]:
        fences += 1
    elif not visited[y - 1][x]:
        next_count, next_fences = dfs((x, y - 1), map, visited, horizontal_fences, vertical_fences)
        count += next_count
        fences += next_fences
    return count, fences

def measure_regions(map, visited, horizontal_fences, vertical_fences):
    total_price = 0
    for y in range(len(visited)):
        for x in range(len(visited[0])):
            if not visited[y][x]:
                count, fences = dfs((x, y), map, visited, horizontal_fences, vertical_fences)
                # print(f"Area of {map[y][x]}: count {count}, fences {fences}")
                total_price += count * fences
    return total_price

if __name__ == "__main__":
    with open("input.txt") as input:
        map, visited, vertical_fences, horizontal_fences = parse_input(input)
    # print(f"Map: ({len(map[0])}, {len(map)})")
    # for line in map:
    #     print(line)
    # print(f"\nVertical fences: ({len(vertical_fences[0])}, {len(vertical_fences)})")
    populate_fences(map, horizontal_fences, vertical_fences)
    # for line in vertical_fences:
    #     print(line)
    # print(f"\nHorizontal fences: ({len(horizontal_fences[0])}, {len(horizontal_fences)})")
    # for line in horizontal_fences:
    #     print(line)
    price = measure_regions(map, visited, horizontal_fences, vertical_fences)
    print(price)