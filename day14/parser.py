def parse_input(input):
    robots = []
    for line in input.readlines():
        line = line.strip("\n").split(" ")
        pos = map(int, line[0].split("=")[1].split(","))
        velocity = map(int, line[1].split("=")[1].split(","))
        robots.append({"pos": [pos_coord for pos_coord in pos], "velocity": [vel_coord for vel_coord in velocity]})
    return robots

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        robots = parse_input(input)
    for rob in robots:
        print(rob)