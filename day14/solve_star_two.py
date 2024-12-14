import numpy as np
import copy
from math import lcm, gcd

def parse_input(input):
    robots = []
    for line in input.readlines():
        line = line.strip("\n").split(" ")
        pos = map(int, line[0].split("=")[1].split(","))
        velocity = map(int, line[1].split("=")[1].split(","))
        robots.append({"pos": [pos_coord for pos_coord in pos], "velocity": [vel_coord for vel_coord in velocity]})
    return robots

def move_robots(robots, map_size):
    for robot in robots:
        robot["pos"][0] += robot["velocity"][0]
        robot["pos"][0] %= map_size[0]
        robot["pos"][1] += robot["velocity"][1]
        robot["pos"][1] %= map_size[1]
    return robots

def move_robots_n_times(robots, map_size, steps):
    for robot in robots:
        robot["pos"][0] += steps * robot["velocity"][0]
        robot["pos"][0] %= map_size[0]
        robot["pos"][1] += steps * robot["velocity"][1]
        robot["pos"][1] %= map_size[1]
    return robots

def find_cycling_periodicity(robot, map_size):
    """
    Detects after how many cycles the robot will cycle onto itself
    For a robot with the following parameters:
                 p0                v0
    position p =    , velocity v =    
                 p1                v1

    With a map of size (N0, N1), we search for the smallest integer k such that:
    (p0 +k*v0)[N0] = p0*N0
    (p1 +k*v1)[N1] = p1*N1

    i.e. k = LCM( N0/GCD(v0, N0) , N1/GCD(v1, N1) )
    """
    (n0, n1) = map_size
    return lcm(n0 // gcd(robot["velocity"][0], n0), n1 // gcd(robot["velocity"][1], n1))

def detect_tree_likelihood(robots, map_size):
    """
    We compute a score, that is supposed to account for the likelihood of the
    current pattern to be a christmas tree.
    The assumption we are making is that the edges of the tree are created
    by aligning :
    - a given robot at position (x, y) with another at position (x - 1, y + 1), another at (x - 2, y + 2), etc [LEFT EDGE]
    - OR a given robot at position (x, y) with another at position (x + 1, y + 1) [RIGHT EDGE]

    This code hence detects patterns like below
    ....#......  .....#......  ....#......
    ...#.#.....  ....#.#.....  ...###.....
    ..#...#....  ...#...#....  ..#####....
    .#.....#...  ..###.###...  .#######...
    ####.####..  ...#...#....  #########..
    ...###.....  ..#.....#...  ...###.....
    ...........  .#########..  ...........

    Returns
    -------
    score: a metric that counts robots that are diagonally adjacent.
    """
    map = [["." for x in range(map_size[0])] for y in range(map_size[1])]
    visited = [[0 for char in line] for line in map]
    for robot in robots:
        pos = robot["pos"]
        if map[pos[1]][pos[0]] == ".":
            map[pos[1]][pos[0]] = 1
        else:
            map[pos[1]][pos[0]] += 1
    for y in range(map_size[1]):
        for x in range(map_size[0]):
            map[y][x] = str(map[y][x])
    score = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            score += count_alignments((x, y), map, visited)
    return score

def left_branch_score(pos, map, visited):
    (x, y) = pos
    visited[y][x] = 1
    if map[y][x] == ".":
        return 0
    elif y < len(map) - 1 and 0 < x:
        return 1 + left_branch_score((x - 1, y + 1), map, visited)
    return 1

def right_branch_score(pos, map, visited):
    (x, y) = pos
    visited[y][x] = 1
    if map[y][x] == ".":
        return 0
    elif y < len(map) - 1 and x < len(map[0]) - 1:
                return 1 + right_branch_score((x + 1, y + 1), map, visited)
    return 1

def count_alignments(pos, map, visited):
    (x, y) = pos
    if not visited[y][x]:
        if map[y][x] == ".":
            return 0
        else:
            visited[y][x] = 1
            next_scores = 0
            if y < len(map) - 1 and 0 < x < len(map[0]) - 1:
                next_scores += left_branch_score((x - 1, y + 1), map, visited) +\
                    right_branch_score((x + 1, y + 1), map, visited)
            return next_scores 
    else:
        return 0

def plot_map(robots, map_size):
    map = [["." for x in range(map_size[0])] for y in range(map_size[1])]
    for robot in robots:
        pos = robot["pos"]
        if map[pos[1]][pos[0]] == ".":
            map[pos[1]][pos[0]] = 1
        else:
            map[pos[1]][pos[0]] += 1
    for y in range(map_size[1]):
        for x in range(map_size[0]):
            map[y][x] = str(map[y][x])
    for row in map:
        print("".join(row))

def detect_tree(robots, map_size, periodicity):
    initial_robots = copy.deepcopy(robots)
    max_score = 0
    max_steps = 0
    for step in range(periodicity + 1):
        score = detect_tree_likelihood(robots, map_size)
        if score > max_score:
            max_score = score
            max_steps = step
        move_robots(robots, map_size)
    move_robots_n_times(initial_robots, map_size, max_steps)
    print(f"Detected tree with max score {max_score} at step {max_steps}")
    plot_map(initial_robots, map_size)

if __name__ == "__main__":
    with open("input.txt") as input:
        robots = parse_input(input)
    map_size = (101, 103)
    # All robots actually cycle with the same periodicity, so we just compute it once.
    periodicity = find_cycling_periodicity(robots[0], map_size)
    detect_tree(robots, map_size, periodicity)