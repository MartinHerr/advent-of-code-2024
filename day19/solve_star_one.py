#!/usr/bin/env python3
from parser import parse_input

def dfs(design, towels):
    # print(f"Cheching {design}")
    if len(design) == 0:
        return True
    max_length = min(len(design), max([towel for towel in towels]))
    for i in range(1, max_length + 1):
        pattern_chunk = design[:i]
        if pattern_chunk in towels[i] and dfs(design[i:], towels):
            return True
    return False

def count_valid_designs(designs, towels):
    count = 0
    for design in designs:
        if dfs(design, towels):
            count += 1
    return count

if __name__ == "__main__":
    with open("input.txt") as input:
        towels, designs = parse_input(input)
        print(towels)
        print(designs)
        print(count_valid_designs(designs, towels))
