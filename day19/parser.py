#!/usr/bin/env python3
def parse_input(input):
    designs = []
    towels = {}
    for i, line in enumerate(input.readlines()):
        line = line.strip("\n")
        if i == 0:
            towels_set = set(line.split(", "))
            for towel in towels_set:
                towel_length = len(towel)
                if towel_length in towels:
                    towels[towel_length].add(towel)
                else:
                    towels[towel_length] = {towel}
        elif i > 1:
            designs.append(line)
    return towels, designs

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        towels, designs = parse_input(input)
        print(towels)
        print(designs)
