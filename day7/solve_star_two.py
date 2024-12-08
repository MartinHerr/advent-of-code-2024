from parser import parse_input

def combine(num1, num2, operator):
    if operator == 0:
        return num1 + num2
    elif operator == 1:
        return num1 * num2
    elif operator == 2:
        return int(str(num1) + str(num2))
    
def ternary(num, max_digits):
    if num == 0:
        return "0" * max_digits
    else:
        ternary_string = ""
        while num > 0:
            ternary_string = str(num % 3) + ternary_string
            num //= 3
        return "0" * (max_digits - len(ternary_string)) + ternary_string

def test_equation(test_value, numbers):
    combinations = 3**(len(numbers) - 1)
    for comb in range(combinations):
        ternary_comb = ternary(comb, len(numbers) - 1)
        int_comb = [int(char) for char in ternary_comb]
        result = numbers[0]
        for i, operator in enumerate(int_comb):
            result = combine(result, numbers[i + 1], operator)
        if result == test_value:
            return True
    return False

def sum_valid_test_values(test_values, numbers):
    result = 0
    for test_value, nums in zip(test_values, numbers):
        if test_equation(test_value, nums):
            result += test_value
    return result

if __name__ == "__main__":
    with open("input.txt") as input:
        test_values, numbers = parse_input(input)
    result = sum_valid_test_values(test_values, numbers)
    print(result)