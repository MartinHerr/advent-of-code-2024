#!/usr/bin/env python3
def parse_input(input):
    links = {}
    seen_computers = set()
    for line in input.readlines():
        connection = line.strip("\n").split("-")
        if connection[0] not in seen_computers:
            links[connection[0]] = [connection[1]]
            if connection[1] not in seen_computers:
                links[connection[1]] = [connection[0]]
            else:
                links[connection[1]].append(connection[0])
        else:
            links[connection[0]].append(connection[1])
            if connection[1] not in seen_computers:
                links[connection[1]] = [connection[0]]
            else:
                links[connection[1]].append(connection[0])
        seen_computers.add(connection[0])
        seen_computers.add(connection[1])
    return seen_computers, links

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        seen_computers, links = parse_input(input)
    for key in seen_computers:
        print(f"{key}: {links[key]}")