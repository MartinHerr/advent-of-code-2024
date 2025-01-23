#!/usr/bin/env python3
from parser import parse_p2_input

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
    
def populate_graph(wires, connections):
    vertices = {}
    for wire, content in wires.items():
        vertex = Vertex(wire)
        vertices.setdefault(wire, vertex)
        vertex.set_leaf(content)
    for con, content in connections.items():
        vertex = Vertex(con)
        vertices.setdefault(con, vertex)
    for con, content in connections.items():
        if content not in [0, 1]:
            vertices[con].set(vertices[content[0]], vertices[content[1]], content[2])
    return vertices

def update_graph(wires, vertices):
    for wire, content in wires.items():
        vertex = vertices[wire]
        if content in [0, 1]:
            vertex.set_leaf(content)
    return vertices

def combine_z_values(vertices):
    z_values = {}
    for name, vertex in vertices.items():
        if vertex.name[0] == "z":
            z_values[vertex.name] = vertex.get_value()
    sorted_z = dict(sorted(z_values.items(), key=lambda pair: -int(pair[0][1:])))
    return "".join([str(value) for _, value in sorted_z.items()])

def compute(x, y, vertices, bit_size=45):
    print(f'Bitwise AND {"{0:b}".format(x)} , {"{0:b}".format(y)}')
    new_wires = {}
    for i in range(bit_size):
        a = i // 10
        b = i % 10
        if i < len("{0:b}".format(x)):
            new_wires[f"x{a}{b}"] = int("{0:b}".format(x)[::-1][i])
        else:
            new_wires[f"x{a}{b}"] = 0
        if i < len("{0:b}".format(y)):
            new_wires[f"y{a}{b}"] = int("{0:b}".format(y)[::-1][i])
        else:
            new_wires[f"y{a}{b}"] = 0
    vertices = update_graph(new_wires, vertices)
    result = combine_z_values(vertices)
    print(f"= {result}")
    return result

def expected_links(rank, all_links):
    """
    Unused function. Recreates all the vertices that compose an adder.
    """
    if rank == 0:
        all_links["z00"] = ["x00", "y00", "XOR"]
        all_links["c01"] = ["x00", "y00", "AND"]
    else:
        byte_a = rank // 10
        byte_b = rank % 10
        next_a = (rank + 1) // 10
        next_b = (rank + 1) % 10
        all_links[f"a{byte_a}{byte_b}"] = [f"x{byte_a}{byte_b}", f"y{byte_a}{byte_b}", "XOR"]
        all_links[f"b{byte_a}{byte_b}"] = [f"x{byte_a}{byte_b}", f"y{byte_a}{byte_b}", "AND"]
        all_links[f"z{byte_a}{byte_b}"] = [f"a{byte_a}{byte_b}", f"c{byte_a}{byte_b}", "XOR"]
        all_links[f"d{byte_a}{byte_b}"] = [f"b{byte_a}{byte_b}", f"c{byte_a}{byte_b}", "AND"]
        all_links[f"c{next_a}{next_b}"] = [f"b{byte_a}{byte_b}", f"d{byte_a}{byte_b}", "OR"]
    
def all_expected_links(rank):
    links = {}
    for r in range(rank):
        expected_links(r, links)
    return links

def detect_non_xor_inputs(links):
    non_xor_z_entries = {key: value for key, value in links.items() if key.startswith("z") and value[-1] != "XOR"}
    return non_xor_z_entries

def detect_other_xor_inputs(links):
    """
    Detects XOR gates that need to be swapped with z gates.
    If we look at how an adder is constructed, the only XOR gates that are allowed
    to be connected to intermediate gates (not x and y gates) are z gates.
    """
    xor_entries = {key: value for key, value in links.items() if not key.startswith("z") and value[-1] == "XOR" and value[0][0] != "x"}
    return xor_entries

def detect_next_vertices(key, links):
    next_vertices = {}
    for i in range(2):
        next_key = links[key][i]
        next_vertices[next_key] = links[next_key]
    return next_vertices

def find_connected_vertex(child_vertex, links):
    result = {}
    for key, value in links.items():
        if value[0] == child_vertex or value[1] == child_vertex:
            result[key] = value
    return result

def swap_entries(key1, key2, links):
    link1 = links[key1]
    link2 = links[key2]
    links[key1] = link2
    links[key2] = link1

if __name__ == "__main__":
    with open("input.txt") as input:
        wires, connections = parse_p2_input(input)
    vertices = populate_graph(wires, connections)
    faulty_z = detect_non_xor_inputs(connections)
    print("""
    Defective z's that don't output the correct value:
    """)
    print(faulty_z)
    print("'z45' is actually correct, since it is the highest weight byte")
    print("""
    These gates are actually z gates:
    """)
    xor_to_swap = detect_other_xor_inputs(connections)
    print(xor_to_swap)
    """
    When manually writing a logic gates adder, we realize that certain properties
    must be true:
    - z{n} must always be connected to a XOR gate
    - except 'z45' which must be connected to an OR gate
    As a result, 'z07', 'z20', 'z28' must be swapped
    One option could be to just swap these with XOR gates that are not connected
    to any x{i}, y{i}
    Hence, we already have 3 swaps:
    vmv <=> z07
    hnv <=> z28
    kfm <=> z20
    """
    print("""
    Swapping gates...
    vmv <=> z07
    hnv <=> z28
    kfm <=> z20
    """)
    swap_entries("vmv", "z07", connections)
    swap_entries("hnv", "z28", connections)
    swap_entries("kfm", "z20", connections)
    vertices = populate_graph(wires, connections)
    compute(2**45 - 1, 2**45 - 1, vertices, bit_size=45)
    print("""
    We still notice an issue with 'z35'. Let's have a look at its child gates:
    """)
    print(detect_next_vertices("z35", connections))
    print("""
    We should have a XOR and an OR gate for each.
    (XOR connected to x{n} and y{n}, OR connected to intermediate nodes as it
    is a carry out byte).
    Instead, {'tqr': ['x35', 'y35', 'AND']} is an intermediate byte that should
    not be the input of z35's XOR gate. Since the other gate is an OR gate, we
    conclude that 'tqr' must be swapped with the vertex that contains ['x35', 'y35', 'XOR']
    """)
    print("""
    We eventually find the vertex 'hth' which needs to be swapped:
    """)
    last_fault_candidates = find_connected_vertex("x35", connections)
    print(last_fault_candidates)
    print("""
    Swapping gates...
    tqr <=> hth
    """)
    swap_entries("tqr", "hth", connections)
    vertices = populate_graph(wires, connections)
    compute(2**45 - 1, 2**45 - 1, vertices, bit_size=45)

    print("\nSorted swapped gates:")
    print(",".join(sorted(["vmv", "z07", "hnv", "z28", "kfm", "z20", "tqr", "hth"])))