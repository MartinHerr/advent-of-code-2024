import re

def parse_input(input):
    pattern = re.compile(r"mul\(\d+,\d+\)")
    mul_matches = []
    for line in input.readlines():
        mul_matches.append(list(map(lambda elt: [int(num) for num in elt[4:-1].split(",")], pattern.findall(line))))
    return mul_matches