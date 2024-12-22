#!/usr/bin/env python3
from parser import parse_input, parse_reduced_input
from copy import deepcopy

def next_orientation(guard):
    if guard == ">":
        return "v"
    elif guard == "v":
        return "<"
    elif guard == "<":
        return "^"
    elif guard == "^":
        return ">"
    else:
        raise ValueError(f"'{guard}' orientation unrecognized for the guard.")

def walk_to_next_wall(
        guard,
        pos,
        walls_positions_by_x,
        walls_positions_by_y,
        map_size):
    (x, y) = pos
    keep_walking = True
    if guard == ">":
        if y in walls_positions_by_y:
            for wall_x in walls_positions_by_y[y]:
                if wall_x > x:
                    return next_orientation(guard), (wall_x - 1, y), keep_walking
        return guard, (map_size[0], y), False
    elif guard == "v":
        if x in walls_positions_by_x:
            for wall_y in walls_positions_by_x[x]:
                if wall_y > y:
                    return next_orientation(guard), (x, wall_y - 1), keep_walking
        return guard, (x, map_size[1]), False
    elif guard == "<":
        if y in walls_positions_by_y:
            for wall_x in walls_positions_by_y[y][::-1]:
                if wall_x < x:
                    return next_orientation(guard), (wall_x + 1, y), keep_walking
        return guard, (-1, y), False
    elif guard == "^":
        if x in walls_positions_by_x:
            for wall_y in walls_positions_by_x[x][::-1]:
                if wall_y < y:
                    return next_orientation(guard), (x, wall_y + 1), keep_walking
        return guard, (x, -1), False
    keep_walking = False

def guard_walk(guard, pos, wall_positions_by_x, wall_positions_by_y, map_size):
    guard_positions_by_x = {pos[0]: [{"dir": guard, "y": pos[1]}]}
    guard_positions_by_y = {pos[1]: [{"dir": guard, "x": pos[0]}]}
    keep_walking = True
    is_cyclic = False
    # print(f"{guard}: {pos}")
    while keep_walking:
        guard, pos, keep_walking = walk_to_next_wall(
            guard, pos, wall_positions_by_x, wall_positions_by_y, map_size)
        (x, y) = pos
        if x in guard_positions_by_x and\
            {"dir": guard, "y": y} in guard_positions_by_x[pos[0]]:
            is_cyclic = True
            keep_walking = False
        if x in guard_positions_by_x:
            guard_positions_by_x[x].append({"dir": guard, "y": y})
        else:
            guard_positions_by_x[x] = [{"dir": guard, "y": y}]
        if y in guard_positions_by_y:
            guard_positions_by_y[y].append({"dir": guard, "x": x})
        else:
            guard_positions_by_y[y] = [{"dir": guard, "x": x}]
        # print(f"{guard}: {pos}")
    return guard_positions_by_x, guard_positions_by_y, is_cyclic

def trap_guard(guard, pos, wall_positions_by_x, wall_positions_by_y, map_size):
    initial_pos = pos
    initial_guard = guard
    count = 0
    cycling_traps_by_x = {}
    # Traps below are cycling traps for the example
    # traps = [(3, 6), (6, 7), (7, 7), (1, 8), (3, 8), (7, 9)]
    while not ((pos[0] in [-1, map_size[0]]) or (pos[1] in [-1, map_size[1]])):
        # print(f"Initial position: {guard}, {pos}")
        # Testing all traps until the next wall is reached
        next_guard, next_pos, _ = walk_to_next_wall(
            guard, pos, wall_positions_by_x, wall_positions_by_y, map_size)
        # print(f"Next position: {next_guard}, {next_pos}")
        (diff_x, diff_y) = (next_pos[0] - pos[0], next_pos[1] - pos[1])
        if abs(diff_x) > 0:
            if diff_x > 0:
                traps = [(x, pos[1]) for x in range(pos[0] + 1, next_pos[0] + 1)]
            elif diff_x < 0:
                traps = [(x, pos[1]) for x in range(pos[0] - 1, next_pos[0] - 1, -1)]
            else:
                traps = []
        elif abs(diff_y) > 0:
            if diff_y > 0:
                traps = [(pos[0], y) for y in range(pos[1] + 1, next_pos[1] + 1)]
            elif diff_y < 0:
                traps = [(pos[0], y) for y in range(pos[1] - 1, next_pos[1] - 1, -1)]
            else:
                traps = []
        else:
            traps = []
        # print(f"Tested traps: {traps}")
        for trap in traps:
            if trap != initial_pos:
                # print(f"Tested trap: {trap}")
                (trap_x, trap_y) = trap
                trap_walls_by_x = deepcopy(wall_positions_by_x)
                trap_walls_by_y = deepcopy(wall_positions_by_y)
                if trap_x in trap_walls_by_x:
                    trap_walls_by_x[trap_x].append(trap_y)
                    trap_walls_by_x[trap_x] = sorted(trap_walls_by_x[trap_x])
                else:
                    trap_walls_by_x[trap_x] = [trap_y]
                if trap_y in trap_walls_by_y:
                    trap_walls_by_y[trap_y].append(trap_x)
                    trap_walls_by_y[trap_y] = sorted(trap_walls_by_y[trap_y])
                else:
                    trap_walls_by_y[trap_y] = [trap_x]
                guard_positions_by_x, guard_positions_by_y, is_cyclic = guard_walk(initial_guard, initial_pos, trap_walls_by_x, trap_walls_by_y, map_size)
                if is_cyclic:
                    if trap[0] in cycling_traps_by_x and\
                        trap[1] in cycling_traps_by_x[trap[0]]:
                        pass
                    else:
                        if trap[0] in cycling_traps_by_x:
                            cycling_traps_by_x[trap[0]].append(trap[1])
                        else:
                            cycling_traps_by_x[trap[0]] = [trap[1]]
                        # print(f"{trap}: Cycle detected!")
                        count += 1
                else:
                    pass
                    # print("Guard left the map.")
                del trap_walls_by_x
                del trap_walls_by_y
        pos = next_pos
        guard = next_guard
    print(count)
    return {}, {}, False

if __name__ == "__main__":
    with open("input.txt") as input:
        guard, pos, wall_positions_by_x, wall_positions_by_y, map_size =\
            parse_reduced_input(input)
    guard_positions_by_x, guard_positions_by_y, is_cyclic = trap_guard(
        guard, pos, wall_positions_by_x, wall_positions_by_y, map_size)
    for x in guard_positions_by_x:
        print(f"{x}: {guard_positions_by_x[x]}")
    for y in guard_positions_by_y:
        print(f"{y}: {guard_positions_by_y[y]}")