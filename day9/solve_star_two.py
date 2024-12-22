#!/usr/bin/env python3
def parse_input(input):
    for line in input.readlines():
        return [int(char) for char in line.strip("\n")]

def store_initial_info(disk_map):
    empty_positions = []
    data_positions = []
    output_array = []
    running_index = 0
    for i, count in enumerate(disk_map):
        if not (i % 2):
            output_array += [i // 2 for _ in range(count)]
            if count > 0:
                data_positions.append({"id": i // 2, "index": running_index, "count": count})
        else:
            output_array += ["." for _ in range(count)]
            if count > 0:
                empty_positions.append({"index": running_index, "count": count})
        running_index += count
    return output_array, data_positions[::-1], empty_positions

def build_memory(output_array, data_positions, empty_positions):
    current_file = None
    while len(data_positions) > 0:
        current_file = data_positions.pop(0)
        if current_file["index"] > empty_positions[0]["index"]:
            for empty_space_rank, empty_space in enumerate(empty_positions):
                # When we find a first match, ONLY to the left of the tested data:
                if empty_space["count"] >= current_file["count"] and\
                    current_file["index"] > empty_space["index"]:
                    # Update output data. Empty the output before rewriting
                    # to avoid the edge case when the "middle" data gets shifted
                    # by shorted than its own length
                    for index in range(
                        current_file["index"],
                        current_file["index"] + current_file["count"]):
                        output_array[index] = "."
                    for index in range(
                        empty_space["index"],
                        empty_space["index"] + current_file["count"]):
                        output_array[index] = current_file["id"]
                    # Update empty space info
                    if empty_space["count"] == current_file["count"]:
                        empty_positions.pop(empty_space_rank)
                    else:
                        empty_space["index"] += current_file["count"]
                        empty_space["count"] -= current_file["count"]
                    # AND leave the loop since we moved the file to the leftmost space
                    break
        # print(output_array)
    return output_array

def checksum(memory):
    result = 0
    for i, block in enumerate(memory):
        if block != ".":
            result += i * block
    return result

if __name__ == "__main__":
    import random
    with open("input.txt") as input:
        disk_map = parse_input(input)
    # disk_map = [random.randint(0, 9) for _ in range(30)]
    # print(f"Disk map: {disk_map}")
    output_array, data_positions, empty_positions = store_initial_info(disk_map)
    # print(output_array)
    # print(f"Data positions: {data_positions}")
    # print(f"Empty positions: {empty_positions}")
    output_array = build_memory(output_array, data_positions, empty_positions)
    # print(f"Output array: {output_array}")
    sum = checksum(output_array)
    print(f"Checksum: {sum}")