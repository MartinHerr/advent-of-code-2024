#!/usr/bin/env python3
import numpy as np
import heapq
from collections import defaultdict
from dijkstra import dijkstra_numeric, dijkstra_direction
from functools import cache

numeric_start = (3, 4)
direction_start = (3, 1)

# input = ["029A", "980A", "179A", "456A", "379A"] # example
input = ["341A", "083A", "802A", "973A", "780A"] # input
# direction_ex = "<A^A>^^AvvvA"

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
    def __init__(self, value):
        self.value = value
        self.children = []
        self.shortest = []

    def add_child(self, child):
        child_node = TreeNode(child)
        self.children.append(child_node)
        return child_node
    
    def __repr__(self):
        return f"TreeNode({self.value}, children={self.children})"
    
    def get_shortest_instruction_length(self):
        if not self.children:
            return len(self.value)
        else:
            if len(self.value) == 1:
                return min([child.get_shortest_instruction_length() for child in self.children])
            elif len(self.value) > 1:
                return sum([child.get_shortest_instruction_length() for child in self.children])

def build_first_tree_layers(code):
    root = TreeNode(code)
    chunks = reconstruct_on_numeric(code)
    leaves = []
    for first_value, first_instructions in zip(code, chunks):
        first_child = root.add_child(first_value)
        for first_instruction in first_instructions:
            second_child = first_child.add_child(first_instruction)
            leaves.append(second_child)
    return root, leaves

def build_next_tree_layers(node):
    code = node.value
    chunks = reconstruct_on_directional(code)
    leaves = []
    for first_value, first_instructions in zip(code, chunks):
        first_child = node.add_child(first_value)
        for first_instruction in first_instructions:
            second_child = first_child.add_child(first_instruction)
            leaves.append(second_child)
    return leaves

def build_whole_tree(code):
    root, leaves = build_first_tree_layers(code)
    for leaf in leaves:
        next_leaves = build_next_tree_layers(leaf)
        for next_leaf in next_leaves:
            next_next_leaves = build_next_tree_layers(next_leaf)
    return root

def sum_complexities(input):
    result = 0
    for code in input:
        numeric_part = int(code[:3])
        root = build_whole_tree(code)
        length = root.get_shortest_instruction_length()
        result += numeric_part * length
    return result

def reconstruct_last_code(input):
    codes = []
    score = 0
    for code in input:
        numeric_part = int(code[:3])
        # print(numeric_part)
        # print(code)
        code_chunks = reconstruct_on_numeric(code)
        next_code_chunks = []
        # print(code_chunks)
        for operation in code_chunks:
            next_code_chunks.append([])
            for possible_instruction in operation:
                next_code_chunks[-1] += reconstruct_on_directional(possible_instruction)
        # print(next_code_chunks)
        # code = reconstruct_on_directional(code)
        # print(code)
        # code = reconstruct_on_directional(code)
        # print(code)
        # codes.append(code)
        # print(f"num: {numeric_part}, len: {len(code)}, score: {numeric_part * len(code)}")
        score += numeric_part * len(code)
    return codes, score

if __name__ == "__main__":
    print(sum_complexities(input))
