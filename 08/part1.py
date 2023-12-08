import os
import re

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = f.readlines()
    directions = re.findall(r"(.)", lines[0])
    path = {
        re.findall(r"(\w+)", line)[0]: re.findall(r"(\w+)", line)[1:]
        for line in lines[2:]
    }

    point = 'AAA'
    direction = 0
    steps = 0

    while point != 'ZZZ':
        left, right = path.get(point)
        point = left if directions[direction] == 'L' else right
        direction = direction + 1 if direction + 1 < len(directions) else 0
        steps += 1

    print(steps)

