#!/usr/bin/env python3
def parse_input(input):
    locks = []
    keys = []
    is_key = False
    is_lock = False
    for line in input.readlines():
        line = line.strip()
        if line == "":
            is_key = False
            is_lock = False
            continue
        if not is_lock and not is_key:
            if line[0] == "#":
                is_lock = True
                locks.append([])
            elif line[0] == ".":
                is_key = True
                keys.append([])
        if is_lock:
            locks[-1].append([])
            for char in line:
                locks[-1][-1].append(char)
        if is_key:
            keys[-1].append([])
            for char in line:
                keys[-1][-1].append(char)
    return locks, keys

def plot_map(map):
    for line in map:
        print("".join(line))

def plot_maps(maps):
    for map in maps:
        for line in map:
            print("".join(line))
        print("\n")

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        locks, keys = parse_input(input)
    plot_maps(locks)
    print("=========")
    plot_maps(keys)