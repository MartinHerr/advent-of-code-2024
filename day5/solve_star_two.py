from parser import parse_input

with open("input.txt") as input:
    orderings, page_numbers = parse_input(input)

def is_correct_update(update):
    if len(update) == 1:
        return True
    else:
        # We are not looking at the case where the order is not specified in
        # the ordering table
        if (update[0] in orderings) and (update[1] in orderings[update[0]]):
            return is_correct_update(update[1:])
        else:
            return False

def sorting_condition(number, reduced_orderings):
    if number in reduced_orderings:
        print(len(reduced_orderings[number]))
        return -len(reduced_orderings[number])
    else:
        return 0

def true_middle_number(update):
    mid_length = (len(update) - 1) // 2
    reduced_orderings = {}
    for num in update:
        if num in orderings:
            reduced_list = []
            for list_num in orderings[num]:
                if list_num in update:
                    reduced_list.append(list_num)
            reduced_orderings[num] = reduced_list
    sorted_update = sorted(
        update, key=lambda x: sorting_condition(x, reduced_orderings))
    print(update)
    print(sorted_update)
    return sorted_update[mid_length]
    
def search_incorrect_updates(page_numbers):
    sum = 0
    for update in page_numbers:
        if not is_correct_update(update):
            sum += true_middle_number(update)
    return sum

if __name__ == "__main__":
    # print(orderings)
    # print(" ")
    print(search_incorrect_updates(page_numbers))