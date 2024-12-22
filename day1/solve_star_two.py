#!/usr/bin/env python3
def parse_input(input):
    list_one = []
    list_two = []
    for line in input.readlines():
        line = line.strip("\n").split("   ")
        list_one.append(int(line[0]))
        list_two.append(int(line[1]))
    return list_one, list_two

def count_appearances(list):
    appearances = {}
    for current_number in list:
        if current_number in appearances:
            appearances[current_number] += 1
        else:
            appearances[current_number] = 1
    return appearances

def search_similarity(list_one, list_two):
    result = 0
    appearances = count_appearances(list_two)
    for current_number in list_one:
        if current_number in appearances:
            result += current_number * appearances[current_number]
    return result


if __name__ == "__main__":
    with open("input.txt") as input:
        l1, l2 = parse_input(input)
    appearances = count_appearances(l2)
    print(appearances)
    similarity = search_similarity(l1, l2)
    print("similarity", similarity)