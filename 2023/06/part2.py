import os
import re

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = f.readlines()
    time = int("".join(re.findall(r"(\d+)", lines[0])))
    distance = int("".join(re.findall(r"(\d+)", lines[1])))
    num_possibilities = sum(
        [
            1 if (speed * (time - speed)) > distance else 0
            for speed in range(0, time + 1)
        ]
    )
    print(num_possibilities)
