#!/usr/bin/env python3
import numpy as np
import math
from parser import parse_input

def tokens_worth_spending(machine, a_cost=3, b_cost=1):
    a = np.array(machine["a"])
    b = np.array(machine["b"])
    p = np.array(machine["prize"])
    system_det = a[0] * b[1] - a[1] * b[0]
    if system_det == 0:
        return 0
    else:
        x_det = b[1] * p[0] - b[0] * p[1]
        y_det = - a[1] * p[0] + a[0] * p[1]
        if x_det % system_det == 0 and y_det % system_det == 0:
            a_steps = x_det // system_det
            b_steps = y_det // system_det
            if a_steps <= 100 and b_steps <= 100:
                return a_steps * a_cost + b_steps * b_cost
        return 0
    
def total_tokens_to_win(machines):
    result = 0
    for machine in machines:
        result += tokens_worth_spending(machine)
    return result

if __name__ == "__main__":
    with open("input.txt") as input:
        machines = parse_input(input)
    result = total_tokens_to_win(machines)
    print(result)