import heapq

def dijkstra(map_2d, current):
    rows, cols = len(map_2d), len(map_2d[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    priority_queue = []
    distances = {}
    visited = set()
    heapq.heappush(priority_queue, (0, current[0], current[1]))
    while priority_queue:
        dist, x, y = heapq.heappop(priority_queue)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if map_2d[y][x] == "O":
            distances[(x, y)] = dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and map_2d[ny][nx] != ".":
                if (nx, ny) not in visited:
                    heapq.heappush(priority_queue, (dist + 1, nx, ny))
    return distances

if __name__ == "__main__":
    map_2d = [
        ["#", "#", "#", "O", "O"],
        ["#", ".", "#", "#", "#"],
        ["#", "#", "#", "#", "O"],
        ["#", "O", "#", ".", "#"],
        ["#", "#", "#", "#", "#"]
    ]
    current = (0, 0)
    result = dijkstra(map_2d, current)
    for target, distance in result.items():
        print(f"Shortest distance to O at {target}: {distance}")