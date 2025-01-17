import os
import re
import math

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = [line.replace('\n', '') for line in f.readlines()]
    bag = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    sum_of_possible_ids = 0
    sum_of_prods = 0

    for line in lines:
        game_id = re.match(r"Game (\d+):", line).group(1)
        game_possibility = []
        cubes_required = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for game in line.split('; '):
            for *_, value, color in re.findall(r"((\d+) (\w+))", game):
                game_possibility.append(int(value) <= bag.get(color))
                if cubes_required.get(color) < int(value):
                    cubes_required.__setitem__(color, int(value))

        sum_of_prods += math.prod(cubes_required.values())

        if all(game_possibility):
            sum_of_possible_ids += int(game_id)

print('part1 =', sum_of_possible_ids)
print('part2 =', sum_of_prods)
