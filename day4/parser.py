def parse_input(input, word_length=4):
    grid = []
    extra_len = word_length - 1
    for count, line in enumerate(input.readlines()):
        if count == 0:
            line_length = 2 * extra_len + len(line) - 1
            for i in range(extra_len):
                grid.append(["." for j in range(line_length)])
        grid.append(
            ["." for i in range(extra_len)] +\
            [char for char in line.strip("\n")] +\
            ["." for i in range(3)])
    for i in range(extra_len):
        grid.append(["." for j in range(line_length)])
    return grid