#!/usr/bin/env python3
import heapq
from collections import defaultdict
from parser import parse_input

def reconstruct_path(came_from, current):
    """Reconstructs the path from start to current node."""
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def neighbors(node, maze):
    """Returns the neighbors of a node."""
    x, y, dir = node
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
    """Computes the cost to move from current to neighbor."""
    return 1 if current[2] == neighbor[2] else 1000

def A_star_find_all_paths(start, goal, h, maze):
    """A* algorithm to find all shortest paths to the goal."""
    came_from = {}
    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0
    f_score = defaultdict(lambda: float("inf"))
    f_score[start] = h(start, goal, maze)
    open_set = []
    heapq.heappush(open_set, (f_score[start], start))

    shortest_paths = []  # Store all shortest paths
    shortest_cost = float("inf")  # Minimum cost to the goal

    while open_set:
        current_f, current = heapq.heappop(open_set)

        # Stop exploring if the current cost exceeds the shortest cost found
        if current_f > shortest_cost:
            break

        x, y, _ = current
        if (x, y) == goal:
            print("Detected goal!")
            current_cost = g_score[current]
            # If the current path has the same cost as the shortest cost, store it
            if current_cost == shortest_cost:
                shortest_paths.append(reconstruct_path(came_from, current))
            # If we find a new shorter cost, reset and store the path
            elif current_cost < shortest_cost:
                shortest_cost = current_cost
                shortest_paths = [reconstruct_path(came_from, current)]
            # Continue exploring for other paths with the same cost
            continue

        for neighbor in neighbors(current, maze):
            tentative_g_score = g_score[current] + distance(current, neighbor)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor, goal, maze)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
            elif tentative_g_score == g_score[neighbor]:
                # If we find an alternative path with the same cost, allow exploration
                print(f"Found alternative candidate with score {f_score[neighbor]}; pusing {neighbor} to the open set.")
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return shortest_paths, shortest_cost

def h(node, goal, maze):
    """Heuristic function (Manhattan distance)."""
    return 0
    # return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# def h(node, goal, maze):
#     # return min(abs(node[1] - goal[1]), abs(node[0] - goal[0]))
#     # Heuristic estimating the cheapest path to the goal
#     # CASE 1 : node and goal are aligned
#     if node[2] == ">" and node[1] == goal[1]:
#         if node[1] <= goal[1]:
#             return abs(goal[0] - node[0]) + abs(goal[1] - node[1])
#         else:
#             return 2000 + abs(node[0] - goal[0]) + abs(goal[1] - node[1])
#     if node[2] == "<" and node[1] == goal[1]:
#         if node[1] >= goal[1]:
#             return abs(goal[0] - node[0]) + abs(goal[1] - node[1])
#         else:
#             return 2000 + abs(node[0] - goal[0]) + abs(goal[1] - node[1])
#     if node[2] == "v" and node[0] == goal[0]:
#         if node[0] <= goal[0]:
#             return abs(goal[0] - node[0]) + abs(goal[1] - node[1])
#         else:
#             return 2000 + abs(goal[0] - node[0]) + abs(node[1] - goal[1]) 
#     if node[2] == "^" and node[0] == goal[0]:
#         if node[0] >= goal[0]:
#             return abs(goal[0] - node[0]) + abs(goal[1] - node[1])
#         else:
#             return 2000 + abs(goal[0] - node[0]) + abs(node[1] - goal[1])
#     # CASE 2: node and goal not aligned, goal in "front" of node
#     if node[2] == ">" and node[0] <= goal[0]:
#         return 1000 + abs(goal[0] - node[0]) + abs(goal[1] - node[1])
#     if node[2] == "<" and node[0] >= goal[0]:
#         return 1000 + abs(goal[0] - node[0]) + abs(goal[1] - node[1])
#     if node[2] == "v" and node[1] <= goal[1]:
#         return 1000 + abs(goal[0] - node[0]) + abs(goal[1] - node[1])
#     if node[2] == "^" and node[1] >= goal[1]:
#         return 1000 + abs(goal[0] - node[0]) + abs(goal[1] - node[1])
#     # CASE 3: node and goal not aligned, goal "behind" node
#     return 2000 + abs(goal[0] - node[0]) + abs(goal[1] - node[1])

def print_paths(paths, map):
    for path in paths:
        for node in path:
            map[node[1]][node[0]] = "O"

def plot_map(map):
    for line in map:
        print("".join(line))

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        map, maze, start, goal = parse_input(input)

    # Run the modified A* algorithm
    paths, cost = A_star_find_all_paths(start, goal, h, maze)

    # Display results
    print(f"Shortest cost: {cost}")
    print(f"Number of shortest paths: {len(paths)}")
    for i, path in enumerate(paths):
        print(f"Path {i + 1}: {path}")
    print_paths(paths, map)
    plot_map(map)