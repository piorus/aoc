import os
import re
import math

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = f.readlines()
    directions = re.findall(r"(.)", lines[0])
    paths = {
        re.findall(r"(\w+)", line)[0]: re.findall(r"(\w+)", line)[1:]
        for line in lines[2:]
    }

    points = [point for point in paths.keys() if point[2] == 'A']
    steps_groups = []

    for point in points:
        direction = 0
        steps = 0

        while point[2] != 'Z':
            left, right = paths.get(point)
            point = left if directions[direction] == 'L' else right
            direction = direction + 1 if direction + 1 < len(directions) else 0
            steps += 1

        steps_groups.append(steps)

    print(math.lcm(*steps_groups))