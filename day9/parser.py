def parse_input(input):
    antennas = {}
    for y, line in enumerate(input.readlines()):
        line = [character for character in line.strip("\n")]
        for x, char in enumerate(line):
            if char != ".":
                if char in antennas:
                    antennas[char].append((x, y))
                else:
                    antennas[char] = [(x, y)]
    return antennas, (x + 1, y + 1)

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        antennas = parse_input(input)
    # print(antennas)