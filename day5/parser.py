#!/usr/bin/env python3
def parse_input(input):
    orderings = {}
    page_numbers = []
    is_second_section = False
    for line in input.readlines():
        line = line.strip("\n")
        if line == "":
            is_second_section = True
        elif not is_second_section:
            [first_num, second_num] = [int(char) for char in line.split('|')]
            if not first_num in orderings:
                orderings[first_num] = [second_num]
            else:
                orderings[first_num].append(second_num)
        else:
            page_numbers.append([int(char) for char in line.split(",")])
    return orderings, page_numbers


if __name__ == "__main__":
    with open("input_ex.txt") as input:
        orderings, page_numbers = parse_input(input)
        print(orderings)
        print(" ")
        for line in page_numbers:
            print(line)