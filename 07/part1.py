import os
import re

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = f.readlines()
    max_rank = len(lines)

    hands = {'fives': [], 'fours': [], 'fullhouses': [], 'threes': [], 'twopairs': [], 'onepairs': [], 'highcard': []}

    encoder = {'A': 'M', 'K': 'L', 'Q': 'K',
               'J': 'J', 'T': 'I', '9': 'H',
               '8': 'G', '7': 'F', '6': 'E',
               '5': 'D', '4': 'C', '3': 'B',
               '2': 'A'}

    for line in lines:
        hand, bet = re.findall(r"(\w+) (\d+)", line)[0]
        cards_in_hand = [encoder.get(card) for card in list(hand)]
        counts_of_cards_in_hand = [cards_in_hand.count(card) for card in set(cards_in_hand)]
        cards_bet_pair = [cards_in_hand, int(bet)]

        if counts_of_cards_in_hand.count(5):
            hands['fives'].append(cards_bet_pair)
        elif counts_of_cards_in_hand.count(4):
            hands['fours'].append(cards_bet_pair)
        elif counts_of_cards_in_hand.count(3) and counts_of_cards_in_hand.count(2):
            hands['fullhouses'].append(cards_bet_pair)
        elif counts_of_cards_in_hand.count(3):
            hands['threes'].append(cards_bet_pair)
        elif counts_of_cards_in_hand.count(2) == 2:
            hands['twopairs'].append(cards_bet_pair)
        elif counts_of_cards_in_hand.count(2) == 1:
            hands['onepairs'].append(cards_bet_pair)
        else:
            hands['highcard'].append(cards_bet_pair)

    for key, values in hands.items():
        hands[key] = sorted(values, key=lambda x: x[0], reverse=True)

    bets = [bet for values in hands.values() for hand, bet in values]
    total_winnings = 0

    for i, bet in enumerate(bets):
        total_winnings += (max_rank - i) * bet

    print(total_winnings)
