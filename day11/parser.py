#!/usr/bin/env python3
def parse_input(input):
    for line in input.readlines():
        stones = [int(char) for char in line.strip("\n").split(" ")]
    return stones


if __name__ == "__main__":
    with open("input_ex.txt") as input:
        stones = parse_input(input)
    print(stones)