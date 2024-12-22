#!/usr/bin/env python3
def parse_input(input):
    numbers = []
    for line in input.readlines():
        numbers.append(int(line.strip("\n")))
    return numbers


if __name__ == "__main__":
    with open("input_ex.txt") as input:
        numbers = parse_input(input)
    for num in numbers:
        print(num)
