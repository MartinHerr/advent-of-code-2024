def parse_map(input):
    map = []
    walls = []
    boxes = []
    for y, line in enumerate(input.readlines()):
        map.append([])
        line = line.strip("\n")
        for x, char in enumerate(line):
            map[-1].append(char)
            if char == "#":
                walls.append((x, y))
            elif char == "O":
                boxes.append((x, y))
            elif char == "@":
                robot = [x, y]
    return map, walls, boxes, robot

def parse_big_map(input):
    map = []
    for y, line in enumerate(input.readlines()):
        map.append([])
        line = line.strip("\n")
        for x, char in enumerate(line):
            if char == "#":
                map[-1].append("#")
                map[-1].append("#")
            elif char == "O":
                map[-1].append("[")
                map[-1].append("]")
            elif char == ".":
                map[-1].append(".")
                map[-1].append(".")
            elif char == "@":
                map[-1].append("@")
                map[-1].append(".")
                robot = [2 * x, y]
    return map, robot

def parse_moves(input):
    return "".join([line.strip("\n") for line in input.readlines()])

if __name__ == "__main__":
    with open("map_ex.txt") as input:
        map, walls, boxes, robot = parse_map(input)
    with open("movements_ex.txt") as input:
        moves = parse_moves(input)
    for line in map:
        print(line)
    print(moves)
    print(f"robot: {robot}")
    print(f"walls: {walls}")
    print(f"boxes: {boxes}")