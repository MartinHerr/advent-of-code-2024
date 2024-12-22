#!/usr/bin/env python3
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

def detect_robots_cycle(robots, map_size, threshold=0.5):
    robots_positions = []
    similarity = 0
    steps_count = 0
    while similarity < threshold:
        current_positions = {}
        for robot in robots:
            (x, y) = tuple(robot["pos"])
            if (x, y) in current_positions:
                current_positions[(x, y)] += 1
            else:
                current_positions[(x, y)] = 1
        robots_positions.append(current_positions)
        for j in range(steps_count):
            similarity = similarity_score(robots_positions[steps_count], robots_positions[j])
        robots = move_robots(robots, map_size)
        steps_count += 1
    return steps_count + 1

def similarity_score(robots_positions_1, robots_positions_2):
    sorted_positions_1 = sorted([key for key in robots_positions_1])
    sorted_positions_2 = sorted([key for key in robots_positions_2])
    index1 = 0
    index2 = 0
    similarity_count = 0
    while index1 < len(sorted_positions_1) and index2 < len(sorted_positions_2):
        if sorted_positions_1[index1] == sorted_positions_2[index2]:
            similarity_count += 1
            index1 += 1
            index2 += 2
        elif sorted_positions_1[index1] < sorted_positions_2[index2]:
            index1 += 1
        else:
            index2 += 1
    return similarity_count / max(len(sorted_positions_1), len(sorted_positions_2))