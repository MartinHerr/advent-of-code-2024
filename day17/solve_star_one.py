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

if __name__ == "__main__":
    # Test example
    print("Test example")
    registers = {"A": 729, "B": 0, "C": 0}
    program = [0, 1, 5, 4, 3, 0]
    output = run_program(registers, program)
    print(f"Registers: {registers}")
    print(f"Program: {program}")
    print(f"Output: {output}")
    print("==========")
    print("Real input")
    registers = {"A": 30899381, "B": 0, "C": 0}
    program = [2,4,1,1,7,5,4,0,0,3,1,6,5,5,3,0]
    output = run_program(registers, program)
    print(f"Registers: {registers}")
    print(f"Program: {program}")
    print(f"Output: {output}")