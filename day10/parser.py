def parse_input(input):
    map = []
    visited = []
    start_positions = []
    for y, line in enumerate(input.readlines()):
        map.append([])
        visited.append([])
        for x, char in enumerate(line.strip("\n")):
            map[-1].append(int(char))
            visited[-1].append(".")
            if int(char) == 0:
                start_positions.append((x, y))
    return map, visited, start_positions


if __name__ == "__main__":
    with open("input_ex.txt") as input:
        map, visited, start_positions = parse_input(input)
    for line in map:
        print(line)
    print(start_positions)