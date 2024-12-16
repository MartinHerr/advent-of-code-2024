import re
import numpy as np

EXAMPLE = 'input_ex.txt'
INPUT = 'input.txt'

pattern = r'-*\d+'
with open(INPUT, 'r') as file : 
    content = file.readlines()

# gridtallness, gridwidth = 7, 11
gridtallness, gridwidth = 103, 101

robots = []
for line in content :
    robots.append([int(k) for k in re.findall(pattern, line)])
# print(robots)

def visualise(robots):
    grid = []
    positions = [[robot[0], robot[1]] for robot in robots]
    for i in range(gridtallness) :
        line = ''
        row = []
        for j in range(gridwidth) :
            if [j, i] in positions : 
                line+=str(positions.count([j, i]))
                row.append(positions.count([j, i]))
            else : 
                line +='.'
                row.append(0)
        grid.append(row)
        print(line)
    return grid




def moverobot1sec(robot):
    x, y, vx, vy = robot[0],robot[1],robot[2],robot[3]
    if x+vx < 0 :
        X = gridwidth + (x+vx)
    elif x+vx >= gridwidth :
        X = (x+vx)%gridwidth
    else : 
        X = x+vx
    if y+vy < 0 :
        Y = gridtallness + (y+vy)
    elif y+vy >= gridtallness :
        Y = (y+vy)%gridtallness
    else : 
        Y = y+vy
    return X, Y

print("")




i=0
minstddev = np.std(robots)
while i<9000:
    robotsmoved = []
    robots_position = []
    for robot in robots :
        moved = moverobot1sec(robot)
        robotsmoved.append([moved[0], moved[1], robot[2], robot[3]])
        robots_position.append(moved)
    robots = robotsmoved[:]
    i+=1
    if np.std(robots_position) < minstddev:
    # if i in range(6375, 6380):
        visualise(robots)
        minstddev = np.std(robots_position)
        print(f"step: {i}, std: {np.std(robots_position)}")