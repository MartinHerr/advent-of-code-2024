#!/usr/bin/env python3
from parser import parse_input

DAY_NUM = 22
DAY_DESC = 'Day 22: Monkey Market'

def next_secret(number):
    number = (number ^ (number * 64)) % 16777216
    number = (number ^ (number // 32)) % 16777216
    number = (number ^ (number * 2048)) % 16777216
    return number

def calc(numbers):
    ret = 0
    total = {}
    for number in numbers:
        last = number % 10
        price_changes = []
        # Storing the list of price changes in price_changes
        for _ in range(2000):
            number = next_secret(number)
            temp = number % 10
            price_changes.append((temp - last, temp))
            last = temp
        # Store patterns seen by the current monkey
        seen_patterns = set()
        # Browsing throug all possible patterns
        for i in range(len(price_changes)-4):
            pattern = tuple(number[0] for number in price_changes[i:i+4])
            sell_value = price_changes[i+3][1]
            if pattern not in seen_patterns:
                seen_patterns.add(pattern)
                if pattern not in total:
                    total[pattern] = sell_value
                else:
                    total[pattern] += sell_value
    ret = max(total.values())
    return ret

if __name__ == "__main__":
    with open("input.txt") as input:
        numbers = parse_input(input)
    print(f"Running day {DAY_DESC}:")
    print(calc(numbers))