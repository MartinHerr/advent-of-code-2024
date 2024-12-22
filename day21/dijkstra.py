import heapq
from functools import cache

@cache
def dijkstra_numeric(current, goal):
    map_2d = [["#", "#", "#", "#", "#"],
              ["#", "7", "8", "9", "#"],
              ["#", "4", "5", "6", "#"],
              ["#", "1", "2", "3", "#"],
              ["#", "#", "0", "A", "#"],
              ["#", "#", "#", "#", "#"]
              ]
    rows, cols = len(map_2d), len(map_2d[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    priority_queue = []
    distances = {}
    visited = set()
    parents = {}  # To store all parents of each node for multiple paths
    heapq.heappush(priority_queue, (0, current[0], current[1]))
    distances[current] = 0
    parents[current] = []
    paths_to_goal = []
    while priority_queue:
        dist, x, y = heapq.heappop(priority_queue)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if map_2d[y][x] == goal:
            # Reconstruct all paths to this goal
            def reconstruct_paths(node):
                if not parents[node]:
                    return [[node]]
                all_paths = []
                for parent in parents[node]:
                    for path in reconstruct_paths(parent):
                        all_paths.append(path + [node])
                return all_paths
            paths_to_goal.extend(reconstruct_paths((x, y)))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and map_2d[ny][nx] != "#":
                new_dist = dist + 1
                if (nx, ny) not in distances or new_dist <= distances[(nx, ny)]:
                    if new_dist < distances.get((nx, ny), float('inf')):
                        distances[(nx, ny)] = new_dist
                        parents[(nx, ny)] = [(x, y)]
                        heapq.heappush(priority_queue, (new_dist, nx, ny))
                    elif new_dist == distances[(nx, ny)]:
                        parents[(nx, ny)].append((x, y))
    return paths_to_goal  # Return all paths to the goal

@cache
def dijkstra_direction(current, goal):
    map_2d = [["#", "#", "#", "#", "#"],
              ["#", "#", "^", "A", "#"],
              ["#", "<", "v", ">", "#"],
              ["#", "#", "#", "#", "#"]]
    rows, cols = len(map_2d), len(map_2d[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    priority_queue = []
    distances = {}
    visited = set()
    parents = {}  # To store all parents of each node for multiple paths
    heapq.heappush(priority_queue, (0, current[0], current[1]))
    distances[current] = 0
    parents[current] = []
    paths_to_goal = []
    while priority_queue:
        dist, x, y = heapq.heappop(priority_queue)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if map_2d[y][x] == goal:
            # Reconstruct all paths to this goal
            def reconstruct_paths(node):
                if not parents[node]:
                    return [[node]]
                all_paths = []
                for parent in parents[node]:
                    for path in reconstruct_paths(parent):
                        all_paths.append(path + [node])
                return all_paths
            paths_to_goal.extend(reconstruct_paths((x, y)))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and map_2d[ny][nx] != "#":
                new_dist = dist + 1
                if (nx, ny) not in distances or new_dist <= distances[(nx, ny)]:
                    if new_dist < distances.get((nx, ny), float('inf')):
                        distances[(nx, ny)] = new_dist
                        parents[(nx, ny)] = [(x, y)]
                        heapq.heappush(priority_queue, (new_dist, nx, ny))
                    elif new_dist == distances[(nx, ny)]:
                        parents[(nx, ny)].append((x, y))
    return paths_to_goal  # Return all paths to the goal