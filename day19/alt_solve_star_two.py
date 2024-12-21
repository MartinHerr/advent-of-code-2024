from functools import cache

with open("input.txt") as input:
    DESIGNS = []
    for i, line in enumerate(input.readlines()):
        line = line.strip("\n")
        if i == 0:
            TOWELS = set(line.split(", "))
        elif i > 1:
            DESIGNS.append(line)

@cache
def get_next_designs(design):
    next_designs = []
    for towel in TOWELS:
        if design.startswith(towel):
            next_designs.append(design[len(towel):])
    return next_designs

def arrangements_bfs(design):
    designs = {design: 1}
    result = 0
    while designs:
        new_designs = {}
        for design, count in designs.items():
            next_designs = get_next_designs(design)
            for next_design in next_designs:
                if next_design == '':
                    result += (len(next_design) + 1) * count
                    continue
                if next_design in new_designs:
                    new_designs[next_design] += count
                else:
                    new_designs[next_design] = count
        designs = new_designs
    return result

def count_arrangements(designs):
    count = 0
    for design in designs:
        count += arrangements_bfs(design)
    return count

if __name__ == "__main__":
    print(count_arrangements(DESIGNS))
