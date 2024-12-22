#!/usr/bin/env python3
def parse_input(input):
    machines = [{}]
    counter = 0
    for line in input.readlines():
        line = "".join(line.strip("\n").split())
        # print(line)
        machine = machines[-1]
        if counter in [0, 1]:
            filtered_line = line.split(":")[-1].split(",")
            x = int(filtered_line[0].split("+")[1])
            y = int(filtered_line[1].split("+")[1])
            if counter == 0:
                key = "a"
            elif counter == 1:
                key = "b"
            machine[key] = (x, y)
        elif counter == 2:
            filtered_line = line.split(":")[-1].split(",")
            x = int(filtered_line[0].split("=")[1])
            y = int(filtered_line[1].split("=")[1])
            key = "prize"
            machine[key] = (x, y)
        elif counter == 3:
            machines.append({})
        counter += 1
        counter %= 4
    return machines

def parse_pt2_input(input):
    machines = [{}]
    counter = 0
    for line in input.readlines():
        line = "".join(line.strip("\n").split())
        # print(line)
        machine = machines[-1]
        if counter in [0, 1]:
            filtered_line = line.split(":")[-1].split(",")
            x = int(filtered_line[0].split("+")[1])
            y = int(filtered_line[1].split("+")[1])
            if counter == 0:
                key = "a"
            elif counter == 1:
                key = "b"
            machine[key] = (x, y)
        elif counter == 2:
            filtered_line = line.split(":")[-1].split(",")
            x = int(filtered_line[0].split("=")[1]) + 10000000000000
            y = int(filtered_line[1].split("=")[1]) + 10000000000000
            key = "prize"
            machine[key] = (x, y)
        elif counter == 3:
            machines.append({})
        counter += 1
        counter %= 4
    return machines

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        machines = parse_input(input)
    for machine in machines:
        print(machine)