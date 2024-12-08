from parser import parse_input
import sys

sys.setrecursionlimit(10000)

WALK_INCREMENTS = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1)
}

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

def guard_walk(guard, pos, count, map):
    # print(f"{guard} : {pos} | {count}")
    (x, y) = pos
    if map[y][x] == "0":
        return count
    else:
        next_x = x + WALK_INCREMENTS[guard][0]
        next_y = y + WALK_INCREMENTS[guard][1]
        if (map[next_y][next_x] == "#"):
            return guard_walk(next_orientation(guard), (x, y), count, map)
        else:
            if map[y][x] == ".":
                count += 1
                map[y][x] = "X"
            return guard_walk(guard, (next_x, next_y), count, map)

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        map, pos, guard = parse_input(input)
    # for line in map:
    #     print(line)
    # print(f"{guard} : {pos}")
    count = guard_walk(guard, pos, 0, map)
    print(count)