from parser import parse_input
from functools import cache

@cache
def dynamic_count(number, n_iters):
    if n_iters == 0:
        return 1
    else:
        if number == 0:
            return dynamic_count(1, n_iters - 1)
        else:
            digits_count = len(str(number))
            if not digits_count % 2:
                left_number = int(number // (10**(digits_count / 2)))
                right_number = int(number - left_number * (10**(digits_count / 2)))
                return dynamic_count(left_number, n_iters - 1) + dynamic_count(right_number, n_iters - 1)
            else:
                return dynamic_count(2024 * number, n_iters - 1)

if __name__ == "__main__":
    with open("input.txt") as input:
        numbers = parse_input(input)
    result = 0
    n_iters = 75
    for num in numbers:
        result += dynamic_count(num, n_iters)
    print(result)