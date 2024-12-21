from functools import cache

def combo(operand, registers):
    # print(f"Calculation combo for operand {operand}")
    if operand in [i for i in range(4)]:
        return operand
    if operand == 4:
        return registers["A"]
    if operand == 5:
        return registers["B"]
    if operand == 6:
        return registers["C"]
    if operand == 7:
        raise ValueError("Combo operand 7 is reserved, program is not valid")

def operate(opcode, operand, pointer, registers, output):
    # adv instruction
    if opcode == 0:
        registers["A"] //= (2**combo(operand, registers))
    # bxl instruction
    elif opcode == 1:
        registers["B"] ^= operand
    # bst instruction
    elif opcode == 2:
        registers["B"] = combo(operand, registers) % 8
    # jnz instruction
    elif opcode == 3:
        if registers["A"] != 0:
            return operand
    # bxc instruction
    elif opcode == 4:
        registers["B"] ^= registers["C"]
    # out instruction
    elif opcode == 5:
        output.append(combo(operand, registers) % 8)
    # bdv instruction
    elif opcode == 6:
        registers["B"] = registers["A"] // (2**combo(operand, registers))
    # cdv instruction
    elif opcode == 7:
        registers["C"] = registers["A"] // (2**combo(operand, registers))
    return pointer + 2


def run_program(registers, program):
    program_length = len(program)
    pointer = 0
    output = []
    while pointer < program_length - 1:
        pointer = operate(program[pointer], program[pointer + 1], pointer, registers, output)
    return output

def first_digit(a):
    program = [2,4,1,1,7,5,4,0,0,3,1,6,5,5,3,0]
    program_length = len(program)
    pointer = 0
    output = []
    registers = {"A": a, "B": 0, "C": 0}
    while pointer < program_length - 1 and len(output) == 0:
            pointer = operate(program[pointer], program[pointer + 1], pointer, registers, output)
    print(f"First digit input a = {a}, output = {output}")
    return output

def find_byte_matches(rank, lower_order_a, program):
    solutions = []
    current_order_a = []
    for j in range(8):
        new_byte = j
        first_digit_value = first_digit(new_byte + 8 * lower_order_a)[0]
        # print(f"Byte value = {j}, New byte = {new_byte}, a = {new_byte + 8 * lower_order_a}, First digit: {first_digit_value} should match {program[len(program) - rank - 1]}")
        if first_digit_value == program[len(program) - rank - 1]:
            print(f"Appending {new_byte + 8 * lower_order_a} to a")
            solutions.append(first_digit_value)
            current_order_a.append(new_byte + 8 * lower_order_a)
    print(f"Found {solutions} as solutions for input {lower_order_a}, a is now {current_order_a}")
    return solutions, current_order_a

def find_a_value(program):
    """
    Successively looking for values of A, such that its bytes satisfy the following
    system.
    first_digit(a >> 3 * i) = program[i]
    for i, an integer between 0 and len(program)
    """
    a_values = [0]
    for i in range(len(program))[::-1]:
        if i == len(program) - 1:
            rank = 0
        else:
            rank = len(oct(a_values[0])) - 2
        print(f"index: {i}, rank: {rank}")
        current_a_values = []
        for a in a_values:
            print(f"Testing with previous rank a = {a}")
            solutions, next_a_values = find_byte_matches(rank, a, program)
            if (next_a_values):
                for new_a in next_a_values:
                    current_a_values.append(new_a)
        a_values = current_a_values
    return solutions, a_values

def test_register_a_init(program):
    program_length = len(program)
    # a = 35184372088832
    a = 0
    while True:
        # Check all A's by incrementing A
        if not a % 10000:
            print(f"Checking A = {a}")
        registers = {"A": a, "B": 0, "C": 0}
        output = []
        pointer = 0
        program_pointer = 0
        to_check = False
        is_equal_to_program = True
        while pointer < program_length - 1:
            # If the program is supposed to output a number, check consistency with the program
            if program[pointer] == 5:
                to_check = True
            pointer = operate(program[pointer], program[pointer + 1], pointer, registers, output)
            if to_check:
                to_check = False
                if len(output) > program_length or output[-1] != program[program_pointer]:
                    is_equal_to_program = False
                    break
                else:
                    program_pointer += 1
        # If the output is shorter than the program, continue
        if len(output) != program_length:
            is_equal_to_program = False
        if is_equal_to_program:
            break
        else:
            a += 1
    return a

if __name__ == "__main__":
    # Test example
    print("Test example")
    program = [0, 3, 5, 4, 3, 0]
    A = test_register_a_init(program)
    print(f"Found A = {A} !")
    registers = {"A": A, "B": 0, "C": 0}
    print(f"Registers: {registers}")
    print(f"Program: {program}")
    print("Running program...")
    output = run_program(registers, program)
    print(f"Registers: {registers}")
    print(f"Output: {output}")
    print("===============")
    for a in range(50):
        print(f"Test value: {first_digit(a)}")
    print(f"Test value: {first_digit(8)}")
    print("===============")
    # Real input
    print("Real input")
    program = [2,4,1,1,7,5,4,0,0,3,1,6,5,5,3,0]

    solutions, a_values = find_a_value(program)
    print("a values")
    print(a_values)
    print(min(a_values))