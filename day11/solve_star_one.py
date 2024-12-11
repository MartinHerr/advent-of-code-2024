from parser import parse_input
from functools import cache

class Stone:
    def __init__(self, number, left=None, right=None):
        self.number = number
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left is not None:
            if self.right is not None:
                return f"({self.left.number})-{self.number}-({self.right.number})"
            else:
                return f"({self.left.number})-{self.number}-(0)"
        else:
            if self.right is not None:
                return f"(0)-{self.number}-({self.right.number})"
            else:
                return f"(0)-{self.number}-(0)"

    def blink(self):
        next_nums = dynamic_blink(self.number)
        self.number = next_nums[0]
        if len(next_nums) == 1:
            next_stone_to_blink = self.right
        else:
            self.right = Stone(next_nums[1], left=self, right=self.right)
            next_stone_to_blink = self.right.right
        return next_stone_to_blink

@cache
def dynamic_blink(number):
    if number == 0:
        return 1,
    else:
        digits_count = len(str(number))
        if not digits_count % 2:
            left_number = int(number // (10**(digits_count / 2)))
            right_number = int(number - left_number * (10**(digits_count / 2)))
            return left_number, right_number
        else:
            return 2024 * number,


def build_stones_chained_list(numbers):
    for i, number in enumerate(numbers):
        if i == 0:
            first_stone = Stone(number)
            current_stone = first_stone
        else:
            previous_stone = current_stone
            current_stone = Stone(number)
            previous_stone.right = current_stone
            current_stone.left = previous_stone
    return first_stone

def print_all_stones(first_stone):
    # count = 0
    current_stone = first_stone
    stones = []
    while current_stone is not None:
        stones.append(current_stone.number)
        # count += 1
        current_stone = current_stone.right
    print(stones)
    # print(f"{count} stones.")

def count_all_stones(first_stone):
    count = 0
    current_stone = first_stone
    while current_stone is not None:
        count += 1
        current_stone = current_stone.right
    print(f"{count} stones.")

def blink_n_times(blink_count, first_stone):
    for _ in range(blink_count):
        current_stone = first_stone
        while current_stone is not None:
            current_stone = current_stone.blink()
        print_all_stones(first_stone)
        # count_all_stones(first_stone)

if __name__ == "__main__":
    # with open("input.txt") as input:
    #     numbers = parse_input(input)
    # first_stone = build_stones_chained_list(numbers)
    # print_all_stones(first_stone)
    # blink_n_times(75, first_stone)
    # count_all_stones(first_stone)
    for i in range(10):
        first_stone = build_stones_chained_list([i])
        print(first_stone)
        blink_n_times(5, first_stone)
        print("===========")
        # print_all_stones(first_stone)