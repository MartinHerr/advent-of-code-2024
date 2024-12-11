def parse_input(input):
    for line in input.readlines():
        return [int(char) for char in line.strip("\n")]

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        disk_map = parse_input(input)
    print(disk_map)