#!/usr/bin/env python3
def parse_input(input):
    list_one = []
    list_two = []
    for line in input.readlines():
        line = line.strip("\n").split("   ")
        list_one.append(int(line[0]))
        list_two.append(int(line[1]))
    return list_one, list_two

def total_distance(list_one, list_two):
    list_one = sorted(list_one)
    list_two = sorted(list_two)
    result = 0
    for i in range(len(list_one)):
        result += abs(list_two[i] - list_one[i])
    return result


if __name__ == "__main__":
    with open("input.txt") as input:
        l1, l2 = parse_input(input)
    print(l1, sorted(l1))
    print(l2)
    distance = total_distance(l1, l2)
    print("distance", distance)