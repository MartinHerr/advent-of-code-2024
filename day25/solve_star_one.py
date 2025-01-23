#!/usr/bin/env python3
import numpy as np
from parser import parse_input, plot_maps

def count_heights(key):
    heights = []
    transposed_key = np.transpose(np.array(key))
    for line in transposed_key:
        heights.append(-1)
        for char in line:
            if char == "#":
                heights[-1] += 1
    return heights

def parse_locks_and_keys_heights(locks, keys):
    locks_heights = []
    keys_heights = []
    for lock in locks:
        locks_heights.append(count_heights(lock))
    for key in keys:
        keys_heights.append(count_heights(key))
    return locks_heights, keys_heights

def count_matches(locks_heights, keys_heights, size=5):
    count = 0
    for lock in locks_heights:
        for key in keys_heights:
            is_valid = True
            for i in range(len(lock)):
                if lock[i] + key[i] > size:
                    is_valid = False
                    break
            if is_valid:
                count += 1
    return count

if __name__ == "__main__":
    with open("input.txt") as input:
        locks, keys = parse_input(input)
    # plot_maps(locks)
    # print("=========")
    # plot_maps(keys)

    locks_heights, keys_heights = parse_locks_and_keys_heights(locks, keys)
    count = count_matches(locks_heights, keys_heights)
    print(count)