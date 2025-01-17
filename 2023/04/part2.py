import os
import re

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = f.readlines()
    games = []
    for line in lines:
        *_, numbers_groups = line.split(':')
        winning_numbers, drawn_numbers = [
            list(map(int, re.findall(r"\d+", numbers_group)))
            for numbers_group in numbers_groups.split('|')
        ]
        games.append({
            'matching_numbers': len(list(set(winning_numbers) & set(drawn_numbers))),
            'copies': 1
        })

    num_games = len(lines)

    for game_id, game in enumerate(games):
        for i in range(game_id + 1, game_id + 1 + game.get('matching_numbers')):
            if i >= num_games:
                break
            games[i]['copies'] = games[i].get('copies') + 1 * game.get('copies')

    total_copies = sum([game.get('copies') for game in games])

    print(total_copies)
