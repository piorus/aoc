import os
import re

bag = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

ids_that_are_possible = []

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = [line.replace('\n', '') for line in f.readlines()]

    for line in lines:
        ID = re.match(r"Game (\d+):", line).group(1)
        game_possibility = []
        games = [
            [
                game_possibility.append(int(value) <= bag.get(color))
                for *_, value, color in re.findall(r"((\d+) (\w+))", game)
            ]
            for game in line.split('; ')
        ]

        if all(game_possibility):
            ids_that_are_possible.append(int(ID))

print(sum(ids_that_are_possible))