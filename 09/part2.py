import os
import re
import math

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = f.readlines()

total = 0

for line in lines:
    sequence = list(map(int, re.findall(r"(-?\d+)", line)))
    diffs = []
    components = []

    found = True

    while not all([num == 0 for num in sequence]):
        diff = [sequence[i + 1] - num for i, num in enumerate(sequence[:-1])]

        try:
            diffs.append(diff[0])
            components.append(sequence[0])
            sequence = diff
        except IndexError:
            found = False
            break

    if not found:
        continue

    last_component = 0
    diff = 0

    for i in range(len(components) - 1, -1, -1):
        diff += diffs[i]
        last_component = components[i] - last_component

    total += last_component

print(total)
