#!/usr/bin/env python3
import numpy as np
import math
from parser import parse_input

def move_robots(robots, map_size, steps):
    for robot in robots:
        robot["pos"][0] += steps * robot["velocity"][0]
        robot["pos"][0] %= map_size[0]
        robot["pos"][1] += steps * robot["velocity"][1]
        robot["pos"][1] %= map_size[1]
    return robots

def safety_factor(robots, map_size):
    # Caution: this function is only true if the map sizes are odd
    top_left_count = 0
    top_right_count = 0
    bottom_left_count = 0
    bottom_right_count = 0
    for robot in robots:
        if robot["pos"][0] < map_size[0] // 2:
            if robot["pos"][1] < map_size[1] // 2:
                top_left_count += 1
            elif robot["pos"][1] > map_size[1] // 2:
                bottom_left_count += 1
        elif robot["pos"][0] > map_size[0] // 2:
            if robot["pos"][1] < map_size[1] // 2:
                top_right_count += 1
            elif robot["pos"][1] > map_size[1] // 2:
                bottom_right_count += 1
    return top_left_count * top_right_count * bottom_left_count * bottom_right_count


if __name__ == "__main__":
    with open("input.txt") as input:
        robots = parse_input(input)
    # for rob in robots:
    #     print(rob)
    # print("========")
    map_size = (101, 103)
    steps = 100
    robots = move_robots(robots, map_size, steps)
    # for rob in robots:
    #     print(rob)
    factor = safety_factor(robots, map_size)
    print(factor)