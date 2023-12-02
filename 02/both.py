import os
import re
import math

bag = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

ids_that_are_possible = []

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = [line.replace('\n', '') for line in f.readlines()]
    sum_of_prods = 0

    for line in lines:
        ID = re.match(r"Game (\d+):", line).group(1)
        game_possibility = []
        cubes_required = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        [
            [
                game_possibility.append(int(value) <= bag.get(color))
                for *_, value, color in re.findall(r"((\d+) (\w+))", game)
            ]
            for game in line.split('; ')
        ]
        [
            [
                cubes_required.__setitem__(color, int(value))
                for *_, value, color in re.findall(r"((\d+) (\w+))", game)
                if cubes_required.get(color) < int(value)
            ]
            for game in line.split('; ')
        ]

        sum_of_prods += math.prod(cubes_required.values())

        if all(game_possibility):
            ids_that_are_possible.append(int(ID))

print('part1 =', sum(ids_that_are_possible))
print('part2 =', sum_of_prods)
