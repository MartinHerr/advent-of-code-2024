def parse_input(input):
    # Parse the schematic into a 2D array
    # We insert a crown of "0" around the array to simplify edge conditions
    schematic = []
    for line_count, line in enumerate(input.readlines()):
        if (line_count == 0):
            # First crown line
            schematic.append(["0" for i in range(len(line.strip("\n")) + 2)])
        # Each line with a "." at beginning and end
        enlarged_line = "0" + line.strip("\n") + "0"
        enlarged_line = [character for character in enlarged_line]
        for x, char in enumerate(enlarged_line):
            if char in ["^", "v", ">", "<"]:
                enlarged_line[x] = "."
                guard_pos = (x, line_count + 1)
                guard = char
        schematic.append(enlarged_line)
    # Last crown line
    schematic.append(["0" for i in range(len(line.strip("\n")) + 2)])
    print(guard_pos)
    return schematic, guard_pos, guard

def parse_reduced_input(input):
    positions_by_x = {}
    positions_by_y = {}
    for y, line in enumerate(input.readlines()):
        for x, char in enumerate([char for char in line]):
            if char in ["^", "v", ">", "<"]:
                start_pos = (x, y)
                guard = char
            if char == "#":
                if x in positions_by_x:
                    positions_by_x[x].append(y)
                else:
                    positions_by_x[x] = [y]
                if y in positions_by_y:
                    positions_by_y[y].append(x)
                else:
                    positions_by_y[y] = [x]
    return guard, start_pos, positions_by_x, positions_by_y, (x + 1, y + 1)

if __name__ == "__main__":
    with open("input.txt") as input:
        guard, guard_pos, positions_by_x, positions_by_y, map_size =\
            parse_reduced_input(input)
    # for line in map:
    #     print(line)
    print(f"{guard} : {guard_pos}")
    print(f"Next walls along same x: {positions_by_x[guard_pos[0]]}")
    print(f"Next walls along same y: {positions_by_y[guard_pos[1]]}")
    print("# positions, sorted by x coordinate")
    for key in positions_by_x:
        print(f"{key}: {positions_by_x[key]}")
    print("# positions, sorted by y coordinate")
    for key in positions_by_y:
        print(f"{key}: {positions_by_y[key]}")
    print(map_size)