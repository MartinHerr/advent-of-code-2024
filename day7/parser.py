def parse_input(input):
    test_values = []
    numbers = []
    for line in input.readlines():
        line = line.strip("\n").split(": ")
        test_values.append(int(line[0]))
        numbers.append([int(char) for char in line[1].split(" ")])
    return test_values, numbers

if __name__ == "__main__":
    with open("input_ex.txt") as input:
        test_values, numbers = parse_input(input)
    for i in range(len(test_values)):
        print(f"{test_values[i]}: {numbers[i]}")