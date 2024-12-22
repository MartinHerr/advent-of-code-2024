#!/usr/bin/env python3
from dijkstra import dijkstra_numeric, dijkstra_direction
from functools import cache

numeric_start = (3, 4)
direction_start = (3, 1)

def move_on_keyboard(path):
    instructions = []
    for i in range(0, len(path) - 1):
        first_key = path[i]
        second_key = path[i + 1]
        if second_key[0] - first_key[0] == 1:
            instructions.append(">")
        elif second_key[0] - first_key[0] == -1:
            instructions.append("<")
        elif second_key[1] - first_key[1] == 1:
            instructions.append("v")
        elif second_key[1] - first_key[1] == -1:
            instructions.append("^")
    instructions.append("A")
    return "".join(instructions)

@cache
def reconstruct_on_numeric(code):
    instructions = []
    start = numeric_start
    for goal in code:
        instructions.append([])
        paths = dijkstra_numeric(start, goal)
        for path in paths:
            instructions[-1].append(move_on_keyboard(path))
        start = path[-1]
    return instructions

@cache
def reconstruct_on_directional(code):
    instructions = []
    start = direction_start
    for goal in code:
        instructions.append([])
        paths = dijkstra_direction(start, goal)
        for path in paths:
            instructions[-1].append(move_on_keyboard(path))
        start = path[-1]
    return instructions

class TreeNode:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.children = []
        self.shortest = float("inf")

    def add_child(self, child):
        child_node = TreeNode(child, self.depth + 1)
        self.children.append(child_node)
        return child_node
    
    def __repr__(self):
        return f"TreeNode({self.value}, depth={self.depth}, shortest={self.shortest}, children={self.children})"
    
    def get_shortest_instruction_length(self):
        if not self.children:
            return len(self.value)
        else:
            if len(self.value) == 1:
                return min([child.get_shortest_instruction_length() for child in self.children])
            elif len(self.value) > 1:
                return sum([child.get_shortest_instruction_length() for child in self.children])

tree_cache = {}

def build_first_tree_layers(code):
    root = TreeNode(code, 0)
    chunks = reconstruct_on_numeric(code)
    leaves = []
    for first_value, first_instructions in zip(code, chunks):
        first_child = root.add_child(first_value)
        for first_instruction in first_instructions:
            second_child = first_child.add_child(first_instruction)
            leaves.append(second_child)
    return root, leaves

# Recursive, depth first build that avoids building nodes whenever possible
def build_next_tree_layers(node, max_depth):
    # When reaching the terminal leaves, compute shortest value and cache
    if node.depth >= max_depth:
        node.shortest = len(node.value)
        tree_cache[(node.value, node.depth)] = node.shortest
        return []
    code = node.value
    # If we cached the current node, do not populate it but immediately
    # access its shortest value
    if (code, node.depth) in tree_cache:
        node.shortest = tree_cache[(code, node.depth)]
        return []
    chunks = reconstruct_on_directional(code)
    # Depth-first populate the child nodes.
    # Compute shortest value on the fly
    for first_value, first_instructions in zip(code, chunks):
        first_child = node.add_child(first_value)
        for first_instruction in first_instructions:
            second_child = first_child.add_child(first_instruction)
            build_next_tree_layers(second_child, max_depth)
            first_child.shortest = min([child.shortest for child in first_child.children])
    node.shortest = sum([child.shortest for child in node.children])
    tree_cache[(code, node.depth)] = node.shortest

def build_whole_tree(code, max_depth):
    root, leaves = build_first_tree_layers(code)
    for leaf in leaves:
        build_next_tree_layers(leaf, max_depth)
    root.shortest = sum(child.shortest for child in root.children)
    return root, root.shortest

def sum_complexities(input, n=25):
    result = 0
    for code in input:
        numeric_part = int(code[:3])
        root, _ = build_whole_tree(code, max_depth=2 * (n + 1))
        # Correctly calculate the length by summing the shortest values of root's children
        length = sum(min(next_child.shortest for next_child in child.children) for child in root.children if child.children)
        result += numeric_part * length
    return result

if __name__ == "__main__":
    # input = ["029A", "980A", "179A", "456A", "379A"] # example
    input = ["341A", "083A", "802A", "973A", "780A"] # input
    print(sum_complexities(input))