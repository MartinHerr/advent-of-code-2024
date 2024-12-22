#!/usr/bin/env python3
import heapq
from collections import defaultdict
from parser import parse_input, diff_output

def dfs(came_from, current, visited):
    # print(f"Searching with DFS on nodes {came_from[current]}")
    visited.add(current)
    for previous_node in came_from[current]:
        dfs(came_from, previous_node, visited)
    return visited

def reconstruct_visited_nodes(came_from, goal):
    """Recursively reconstructs all shortest paths."""
    # Add a last node pointing to all end nodes with directions
    terminal_nodes = []
    for node in came_from:
        if (node[0], node[1]) == goal:
            terminal_nodes.append(node)
    came_from[(goal[0], goal[1], "E")] = terminal_nodes
    oriented_nodes = dfs(came_from, (goal[0], goal[1], "E"), set())
    visited_nodes = set()
    for node in oriented_nodes:
        visited_nodes.add((node[0], node[1]))
    return visited_nodes

def neighbors(node, maze):
    """Returns the neighbors of a node."""
    x, y, direction = node
    next_neighbors = []
    if direction == ">":
        if maze[(x + 1, y)] != "#":
            next_neighbors.append((x + 1, y, ">"))
        if maze[(x, y - 1)] != "#":
            next_neighbors.append((x, y, "^"))
        if maze[(x, y + 1)] != "#":
            next_neighbors.append((x, y, "v"))
    elif direction == "<":
        if maze[(x - 1, y)] != "#":
            next_neighbors.append((x - 1, y, "<"))
        if maze[(x, y - 1)] != "#":
            next_neighbors.append((x, y, "^"))
        if maze[(x, y + 1)] != "#":
            next_neighbors.append((x, y, "v"))
    elif direction == "^":
        if maze[(x, y - 1)] != "#":
            next_neighbors.append((x, y - 1, "^"))
        if maze[(x + 1, y)] != "#":
            next_neighbors.append((x, y, ">"))
        if maze[(x - 1, y)] != "#":
            next_neighbors.append((x - 1, y, "<"))
    elif direction == "v":
        if maze[(x, y + 1)] != "#":
            next_neighbors.append((x, y + 1, "v"))
        if maze[(x + 1, y)] != "#":
            next_neighbors.append((x + 1, y, ">"))
        if maze[(x - 1, y)] != "#":
            next_neighbors.append((x - 1, y, "<"))
    return next_neighbors[::-1]

def distance(current, neighbor):
    """Computes the cost to move from current to neighbor."""
    return 1 if current[2] == neighbor[2] else 1000

def Dijkstra_find_all_shortest_paths(start, goal, maze):
    """A* algorithm to find all shortest paths to the goal."""
    # Priority queue
    open_set = []
    heapq.heappush(open_set, (0, start))
    # Cost tracking
    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0
    # Multiple predecessors tracking
    came_from = defaultdict(list)
    # Track nodes that belong to shortest paths
    shortest_nodes = set()
    shortest_cost = float("inf")
    while open_set:
        current_cost, current = heapq.heappop(open_set)
        # Stop processing if cost exceeds the shortest found cost
        if current_cost > shortest_cost:
            break
        x, y, _ = current
        # If the goal is reached
        if (x, y) == goal:
            if current_cost < shortest_cost:
                # Found a new shortest cost
                shortest_cost = current_cost
            shortest_nodes.add((x, y))
            continue
        # Explore neighbors
        for neighbor in neighbors(current, maze):
            nx, ny, _ = neighbor
            tentative_cost = g_score[current] + distance(current, neighbor)
            if tentative_cost < g_score[neighbor]:
                # Found a better path to neighbor
                g_score[neighbor] = tentative_cost
                came_from[neighbor] = [current]  # Replace predecessors
                heapq.heappush(open_set, (tentative_cost, neighbor))
            elif tentative_cost == g_score[neighbor]:
                # Found an alternative path with the same cost
                came_from[neighbor].append(current)
    visited_nodes = reconstruct_visited_nodes(came_from, goal)
    return visited_nodes, shortest_cost

def plot_map(map):
    """Prints the maze map."""
    for line in map:
        print("".join(line))

def print_nodes(nodes, map):
    for node in nodes:
        map[node[1]][node[0]] = "O"

if __name__ == "__main__":
    with open("input.txt") as input:
        map, maze, start, goal = parse_input(input)
    print("Initial Map:")
    plot_map(map)
    visited_nodes, shortest_cost = Dijkstra_find_all_shortest_paths(start, goal, maze)
    print_nodes(visited_nodes, map)
    print("\nMap After Marking Shortest Paths:")
    plot_map(map)

    print(f"\nShortest cost: {shortest_cost}")
    print(f"Number of shortest paths nodes: {len(visited_nodes)}")

    with open("map_sur_input_martin.txt") as output:
        print(len(map[0]), len(map))
        diffs = diff_output(map, output)
        print(diffs)
