#!/usr/bin/env python3
from parser import parse_input

def populate_fences(map, horizontal_fences, vertical_fences):
    (map_y, map_x) = (len(map), len(map[0]))
    for y, line in enumerate(map):
        for x, _ in enumerate(line):
            if x < map_x - 1 and map[y][x] != map[y][x + 1]:
                vertical_fences[y][x + 1] = 1
            if y < map_y - 1 and map[y][x] != map[y + 1][x]:
                horizontal_fences[y + 1][x] = 1
    return horizontal_fences, vertical_fences

def dfs(start_pos, map, visited, horizontal_fences, vertical_fences):
    (x, y) = start_pos
    count = 1
    local_vertical_fences = []
    local_horizontal_fences = []
    visited[y][x] = 1
    # Search right
    if vertical_fences[y][x + 1]:
        local_vertical_fences.append((x + 1, y, "R"))
    elif not visited[y][x + 1]:
        next_count, next_horizontal_fences, next_vertical_fences = dfs((x + 1, y), map, visited, horizontal_fences, vertical_fences)
        count += next_count
        local_horizontal_fences += next_horizontal_fences
        local_vertical_fences += next_vertical_fences
    # Search down
    if horizontal_fences[y + 1][x]:
        local_horizontal_fences.append((x, y + 1, "D"))
    elif not visited[y + 1][x]:
        next_count, next_horizontal_fences, next_vertical_fences = dfs((x, y + 1), map, visited, horizontal_fences, vertical_fences)
        count += next_count
        local_horizontal_fences += next_horizontal_fences
        local_vertical_fences += next_vertical_fences
    # Search left
    if vertical_fences[y][x]:
        local_vertical_fences.append((x, y, "L"))
    elif not visited[y][x - 1]:
        next_count, next_horizontal_fences, next_vertical_fences = dfs((x - 1, y), map, visited, horizontal_fences, vertical_fences)
        count += next_count
        local_horizontal_fences += next_horizontal_fences
        local_vertical_fences += next_vertical_fences
    # Search up
    if horizontal_fences[y][x]:
        local_horizontal_fences.append((x, y, "U"))
    elif not visited[y - 1][x]:
        next_count, next_horizontal_fences, next_vertical_fences = dfs((x, y - 1), map, visited, horizontal_fences, vertical_fences)
        count += next_count
        local_horizontal_fences += next_horizontal_fences
        local_vertical_fences += next_vertical_fences
    return count, local_horizontal_fences, local_vertical_fences

def count_horizontal_fences(fences):
    fences = sorted(fences, key=lambda pos: 1000 * pos[1] + pos[0])
    # print(f"H fences: {fences}")
    count = 0
    previous_fence = None
    for fence in fences:
        if previous_fence is None:
            count += 1
            # print(f"New fence detected (previous fence is None) : {fence}")
        else:
            if fence[1] == previous_fence[1]:
                if abs(fence[0] - previous_fence[0]) == 1:
                    if fence[2] == previous_fence[2]:
                        pass
                    else:
                        count += 1
                        # print(f"New fence detected (opposite orientations) : {fence}")
                else:
                    count += 1
                    # print(f"New fence detected (diff is greated than 1) : {fence}")
            else:
                count += 1
                previous_fence = fence
                # print(f"New fence detected (new y) : {fence}")
        previous_fence = fence
    return count

def count_vertical_fences(fences):
    fences = sorted(fences, key=lambda pos: 1000 * pos[0] + pos[1])
    # print(f"V fences: {fences}")
    count = 0
    previous_fence = None
    for fence in fences:
        if previous_fence is None:
            count += 1
            # print(f"New fence detected (previous fence is None) : {fence}")
        else:
            if fence[0] == previous_fence[0]:
                if abs(fence[1] - previous_fence[1]) == 1:
                    if fence[2] == previous_fence[2]:
                        pass
                    else:
                        count += 1
                        # print(f"New fence detected (opposite orientations) : {fence}")
                else:
                    count += 1
                    # print(f"New fence detected (diff is greated than 1) : {fence}")
            else:
                count += 1
                previous_fence = fence
                # print(f"New fence detected (new x) : {fence}")
        previous_fence = fence
    return count

def measure_regions(map, visited, horizontal_fences, vertical_fences):
    total_price = 0
    for y in range(len(visited)):
        for x in range(len(visited[0])):
            if not visited[y][x]:
                count, local_horizontal_fences, local_vertical_fences = dfs((x, y), map, visited, horizontal_fences, vertical_fences)
                # print("Horizontal fences:")
                # print(local_horizontal_fences)
                horizontal_fences_count = count_horizontal_fences(local_horizontal_fences)
                # print("Vertical fences:")
                # print(local_vertical_fences)
                vertical_fences_count = count_vertical_fences(local_vertical_fences)
                fences = horizontal_fences_count + vertical_fences_count
                # print(f"\nArea of {map[y][x]}: count {count}, fences {fences}")
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