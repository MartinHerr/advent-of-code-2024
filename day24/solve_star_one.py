#!/usr/bin/env python3
from parser import parse_input

class Vertex:
    def __init__(self, name):
        self.name = name
        self.operand = ""
        self.value = None
        self.childs = []
    
    def __repr__(self):
        if self.childs != []:
            return f"{self.name}: {self.childs[0].name}, {self.childs[1].name}, {self.operand}"
        else:
            return f"{self.name}: {self.value}"
    
    def set_leaf(self, value):
        self.value = value
    
    def set(self, child1, child2, operand):
        self.childs = [child1, child2]
        self.operand = operand

    def get_value(self):
        if self.value is not None:
            return self.value
        else:
            if self.operand == "":
                raise ValueError("Vertex not populated.")
            if self.operand == "AND":
                return self.childs[0].get_value() & self.childs[1].get_value()
            if self.operand == "OR":
                return self.childs[0].get_value() | self.childs[1].get_value()
            if self.operand == "XOR":
                return self.childs[0].get_value() ^ self.childs[1].get_value()
    
def populate_graph(wires):
    vertices = {}
    for wire, content in wires.items():
        vertex = Vertex(wire)
        vertices.setdefault(wire, vertex)
        if content in [0, 1]:
            vertex.set_leaf(content)
    for wire, content in wires.items():
        if content not in [0, 1]:
            vertices[wire].set(vertices[content[0]], vertices[content[1]], content[2])
    return vertices

def combine_z_values(vertices):
    z_values = {}
    for name, vertex in vertices.items():
        if vertex.name[0] == "z":
            z_values[vertex.name] = vertex.get_value()
    sorted_z = dict(sorted(z_values.items(), key=lambda pair: -int(pair[0][1:])))
    return int("".join([str(value) for _, value in sorted_z.items()]), 2)


if __name__ == "__main__":
    with open("input.txt") as input:
        wires = parse_input(input)
    # print(wires)
    vertices = populate_graph(wires)
    output = combine_z_values(vertices)
    # for key, value in vertices.items():
    #     print(f"{value}")
    print("=========")
    print(output)
    # for key, value in output.items():
    #     print(f"{key}: {value}")