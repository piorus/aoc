import os
import re
import math

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = f.readlines()
    times = list(map(int, re.findall(r"(\d+)", lines[0])))
    distances = list(map(int, re.findall(r"(\d+)", lines[1])))
    num_possibilities = []

    for time, distance in list(zip(times, distances)):
        num_possibilities.append(
            sum(
                [
                    1 if (speed * (time - speed)) > distance else 0
                    for speed in range(0, time + 1)
                ]
            )
        )
    print(math.prod(num_possibilities))
