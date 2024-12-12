def parse_input(input):
    map = []
    visited = []
    for y, line in enumerate(input.readlines()):
        map.append([])
        visited.append([])
        for x, char in enumerate(line.strip("\n")):
            map[-1].append(char)
            visited[-1].append(0)
    vertical_fences = [[0 for x in range(len(map[0]) + 1)] for y in range(len(map))]
    for _, line in enumerate(vertical_fences):
        line[0] = 1
        line[-1] = 1
    horizontal_fences = [[0 for x in range(len(map[0]))] for y in range(len(map) + 1)]
    for y, line in enumerate(horizontal_fences):
        for x, fence in enumerate(line):
            if y == 0 or y == len(horizontal_fences) - 1:
                line[x] = 1
    return map, visited, vertical_fences, horizontal_fences


if __name__ == "__main__":
    with open("input_ex.txt") as input:
        map, visited, vertical_fences, horizontal_fences = parse_input(input)
    for line in map:
        print(line)
    print(f"Map: ({len(map[0])}, {len(map)})")
    for line in vertical_fences:
        print(line)
    print(f"Vertical fences: ({len(vertical_fences[0])}, {len(vertical_fences)})")
    for line in horizontal_fences:
        print(line)
    print(f"Horizontal fences: ({len(horizontal_fences[0])}, {len(horizontal_fences)})")
    