#!/usr/bin/env python3
from parser import parse_input
from collections import deque


def dfs(design, towels):
    print(f"Cheching {design}")
    valid_branches = 0
    if len(design) == 0:
        return 1
    max_length = min(len(design), max([towel for towel in towels]))
    for i in range(1, max_length + 1):
        pattern_chunk = design[:i]
        if pattern_chunk in towels[i]:
            valid_sub_branches = dfs(design[i:], towels)
            valid_branches += valid_sub_branches
    return valid_branches

def count_arrangements(designs, towels):
    count = 0
    for design in designs:
        print(f"Checking design {design}")
        count += dfs(design, towels)
    return count

if __name__ == "__main__":
    with open("input.txt") as input:
        towels, designs = parse_input(input)
        # print(towels)
        # print(designs)
        print(count_arrangements(designs, towels))
