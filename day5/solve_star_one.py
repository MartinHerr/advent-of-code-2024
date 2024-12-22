#!/usr/bin/env python3
from parser import parse_input

def is_correct_update(orderings, update):
    if len(update) == 1:
        return True
    else:
        # We are not looking at the case where the order is not specified in
        # the ordering table
        if (update[0] in orderings) and (update[1] in orderings[update[0]]):
            return is_correct_update(orderings, update[1:])
        else:
            return False

def middle_number(update):
    if not len(update) % 2:
        raise ValueError("The update length is even; there is no middle number.")
    else:
        return update[(len(update) - 1) // 2]
    
def search_correct_updates(orderings, page_numbers):
    sum = 0
    for update in page_numbers:
        if is_correct_update(orderings, update):
            sum += middle_number(update)
    return sum

if __name__ == "__main__":
    with open("input.txt") as input:
        orderings, page_numbers = parse_input(input)
    print(search_correct_updates(orderings, page_numbers))