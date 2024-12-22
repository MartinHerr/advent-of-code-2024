#!/usr/bin/env python3
from collections import Counter

with open("input.txt") as f:
    data = list(map(int, f.read().strip().split()))
demo_data = [125, 17]


def solve(numbers, steps):
    counter = Counter(numbers)
    for _ in range(steps):
        step_counter = Counter()
        for number, count in counter.items():
            str_n = str(number)
            if number == 0:
                step_counter[1] += count
            elif len(str_n) % 2 == 0:
                middle = len(str_n) // 2
                step_counter[int(str_n[:middle])] += count
                step_counter[int(str_n[middle:])] += count
            else:
                step_counter[number * 2024] += count
        counter = step_counter

    return sum([step_counter[key] for key in step_counter])


demo_res = solve(demo_data, 25)
assert demo_res == 55312, demo_res

res = solve(data, 75)
print(res)