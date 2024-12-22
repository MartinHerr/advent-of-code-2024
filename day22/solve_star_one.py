from parser import parse_input

def next_secret(number):
    number = (number ^ (number * 64)) % 16777216
    number = (number ^ (number // 32)) % 16777216
    number = (number ^ (number * 2048)) % 16777216
    return number

def generate_daily_secret(number, iterations=2000):
    for _ in range(iterations):
        number = next_secret(number)
    return number

def score(numbers):
    result = 0
    for number in numbers:
        result += generate_daily_secret(number)
    return result

if __name__ == "__main__":
    with open("input.txt") as input:
        numbers = parse_input(input)
    print(score(numbers))