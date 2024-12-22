#!/usr/bin/env python3
from parser import parse_input

def build_memory(disk_map):
    left_pointer = 0
    right_pointer = len(disk_map) - 1
    left_id = 0
    right_id = len(disk_map) // 2
    left_count = disk_map[left_pointer]
    right_count = disk_map[right_pointer]
    memory = []
    digits_to_append = []
    while left_pointer < right_pointer:
        # Append left IDs
        memory += [left_id for _ in range(left_count)]
        # Append right IDs until there is no more free memory
        left_pointer += 1
        left_count = disk_map[left_pointer]
        for i in range(left_count):
            digits_to_append.append(right_id)
            right_count -= 1
            if right_count == 0:
                right_pointer -= 2
                right_count = disk_map[right_pointer]
                right_id -= 1
        memory += digits_to_append
        digits_to_append = []
        left_pointer += 1
        left_count = disk_map[left_pointer]
        left_id += 1
    print(f"left pointer: {left_pointer}, left id: {left_id}, left count: {left_count}")
    print(f"right pointer: {right_pointer}, right id: {right_id}, right count: {right_count}")
    if left_pointer <= right_pointer:
        memory += [right_id for _ in range(right_count)]
    return memory

def checksum(memory):
    result = 0
    for i, block in enumerate(memory):
        result += i * block
    return result

if __name__ == "__main__":
    with open("input.txt") as input:
        disk_map = parse_input(input)
    print(disk_map)
    memory = build_memory(disk_map)
    print(memory[:100])
    sum = checksum(memory)
    print(sum)