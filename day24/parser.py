#!/usr/bin/env python3
def parse_input(input):
    wires = {}
    connections = {}
    next_part = False
    for line in input.readlines():
        line = line.strip()
        if line == "":
            next_part = True
            continue
        if not next_part:
            wire, state = line.split(": ")
            state = int(state)
            wires.setdefault(wire, state)
        else:
            wire1, operator, wire2, _, end_wire = line.split(" ")
            wires.setdefault(end_wire, [wire1, wire2, operator])
    return wires

def parse_p2_input(input):
    wires = {}
    connections = {}
    next_part = False
    for line in input.readlines():
        line = line.strip()
        if line == "":
            next_part = True
            continue
        if not next_part:
            wire, state = line.split(": ")
            state = int(state)
            wires.setdefault(wire, state)
        else:
            wire1, operator, wire2, _, end_wire = line.split(" ")
            current_wires = sorted([wire1, wire2])
            connections.setdefault(end_wire, [current_wires[0], current_wires[1], operator])
    return wires, connections

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        wires = parse_input(input)
    print(wires)