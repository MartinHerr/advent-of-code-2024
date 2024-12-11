from parser import parse_input

def find_valid_neighbors(position: tuple[int], map_size: tuple[int]):
    (x, y) = position
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    filtered_neighbors = []
    for neighbor in neighbors:
        (scan_x, scan_y) = neighbor
        if 0 <= scan_x < map_size[0] and 0 <= scan_y < map_size[1]:
            filtered_neighbors.append(neighbor)
    return filtered_neighbors

def walk_map(position: tuple[int],
             start_node: tuple[int],
             map: list,
             visited: list[list],
             map_size: tuple[int]):
    head = map[position[1]][position[0]]
    # print(f"Head: {head}, position: {position}")
    if head != 9:
        neighbors = find_valid_neighbors(position, map_size)
        # print(f"Scanning neighbors: {neighbors}")
        local_score = 0
        for (next_x, next_y) in neighbors:
            if map[next_y][next_x] == head + 1:
                if visited[next_y][next_x] == ".":                
                    local_score += walk_map((next_x, next_y), start_node, map, visited, map_size)
                # And add the result to local score
        # visited[position[1]][position[0]] = local_score
    else:
        local_score = 1
    visited[position[1]][position[0]] = local_score
    # print(f"Head: {head}, position: {position}, score: {local_score}")
    return local_score

def walk_from_all_starts(start_positions, map, visited, map_size):
    result = 0
    for start_position in start_positions:
        result += walk_map(start_position, start_position, map, visited, map_size)
        visited = [["." for _ in line] for line in visited]
    return result

if __name__ == "__main__":
    with open("input.txt") as input:
        map, visited, start_positions = parse_input(input)
    for line in map:
        print(line)
    print("========================")
    print(start_positions)
    map_size = (len(map[0]), len(map))
    score = walk_from_all_starts(start_positions, map, visited, map_size)
    # for line in visited:
    #     print(line)
    print(f"Score: {score}")