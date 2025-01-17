import os
import re

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    total_points = 0
    for line in f.readlines():
        *_, numbers_groups = line.split(':')
        winning_numbers, drawn_numbers = [
            list(map(int, re.findall(r"\d+", numbers_group)))
            for numbers_group in numbers_groups.split('|')
        ]
        intersected_numbers = list(set(winning_numbers) & set(drawn_numbers))
        total_points += 2**(len(intersected_numbers)-1) if len(intersected_numbers) > 0 else 0
    print(total_points)