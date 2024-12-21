from parser import parse_input
from dijkstra import dijkstra

def manhattan(tile1, tile2):
    dx = abs(tile1[0] - tile2[0])
    dy = abs(tile1[1] - tile2[1])
    return dx + dy

class Tile:
    def __init__(self, position, picoseconds, parent_tile=None):
        self.x = position[0]
        self.y = position[1]
        self.picoseconds = picoseconds
        self.parent = parent_tile
    
    def __repr__(self):
        return f"({self.x}, {self.y}), ps={self.picoseconds}, parent={self.parent.get_pos()}"

    def get_pos(self):
        return (self.x, self.y)
    
def find_next_pos(tile, map, previous_tile=None):
    next_positions = {
        (tile.x + 1, tile.y),
        (tile.x - 1, tile.y),
        (tile.x, tile.y + 1),
        (tile.x, tile.y - 1)
    }
    if previous_tile is not None:
        next_positions.remove(previous_tile.get_pos())
    for pos in next_positions:
        if map[pos[1]][pos[0]] == ".":
            return pos
    return (-1, -1)

def reduced_map(tile, map, size=20):
    rows, cols = len(map), len(map[0])
    goals = []
    reduced = []
    for y in range(max(0, tile.y - size), min(rows, tile.y + size + 1)):
        reduced.append([])
        for x in range(max(0, tile.x - size), min(cols, tile.x + size + 1)):
            if map[y][x] == "O":
                reduced[-1].append(".")
                goals.append((x, y))
            else:
                reduced[-1].append(map[y][x])
    return reduced, goals

def build_path(map, start, end, size=20, threshold=50):
    cheats = {}
    # Building Start tile
    pos = start
    tiles = {}
    picoseconds = 0
    current = Tile(pos, picoseconds)
    map[pos[1]][pos[0]] = "O"
    tiles[current.get_pos()] = current
    pos = find_next_pos(current, map)
    # Building tiles
    while pos != (-1, -1):
        picoseconds += 1
        previous = current
        current = Tile(pos, picoseconds, parent_tile=previous)
        map[pos[1]][pos[0]] = "O"
        tiles[current.get_pos()] = current
        pos = find_next_pos(current, map, previous_tile=previous)
        reduced, goals = reduced_map(current, map, size=size)
        trials = {}
        for goal in goals:
            trials[goal] = manhattan(goal, current.get_pos())
        for trial in trials:
            normal_path_length = current.picoseconds - tiles[trial].picoseconds
            cheat = normal_path_length - trials[trial]
            if cheat > 0 and trials[trial] <= size:
                if cheat in cheats:
                    cheats[cheat] += 1
                else:
                    cheats[cheat] = 1
    # Building End tile
    pos = end
    picoseconds += 1
    previous = current
    current = Tile(pos, picoseconds, parent_tile=previous)
    tiles[current.get_pos()] = current
    reduced, goals = reduced_map(current, map, size=size)
    trials = {}
    for goal in goals:
        trials[goal] = manhattan(goal, current.get_pos())
    for trial in trials:
        normal_path_length = current.picoseconds - tiles[trial].picoseconds
        cheat = normal_path_length - trials[trial]
        if cheat > 0 and trials[trial] <= size:
            if cheat in cheats:
                cheats[cheat] += 1
            else:
                cheats[cheat] = 1
    return cheats

def count_supercheats(map, start, end, threshold=50):
    count = 0
    cheats = build_path(map, start, end, threshold=threshold)
    for cheat in sorted([cheat for cheat in cheats]):
        print(f"cheat length: {cheat}, count: {cheats[cheat]}")
    for cheat in cheats:
        if cheat >= threshold:
            count += cheats[cheat]
    return count

def plot_map(map):
    for line in map:
        print("".join(line))

if __name__ == "__main__":
    with open("input.txt") as input:
        map, maze, start, end = parse_input(input)
    plot_map(map)
    supercheats = count_supercheats(map, start, end, threshold=100)
    plot_map(map)
    print(supercheats)