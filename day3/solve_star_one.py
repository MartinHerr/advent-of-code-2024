from parser import parse_input

def compute_mults(numbers):
    result = 0
    for line in numbers:
        for num in line:
            result += num[0] * num[1]
    return result

if __name__ == "__main__":
    with open("input.txt") as input:
        numbers = parse_input(input)
        result = compute_mults(numbers)
        print(result)