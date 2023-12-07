import os
import re

with open('{}/input'.format(os.path.dirname(__file__)), 'r') as f:
    lines = f.readlines()
    max_rank = len(lines)

    hands = {'fives': [], 'fours': [], 'fullhouses': [], 'threes': [], 'twopairs': [], 'onepairs': [], 'highcard': []}

    encoder = {'A': 'M', 'K': 'L', 'Q': 'K',
               'T': 'J', '9': 'I',
               '8': 'H', '7': 'G', '6': 'F',
               '5': 'E', '4': 'D', '3': 'C',
               '2': 'B', 'J': 'A'}

    for line in lines:
        hand, bet = re.findall(r"(\w+) (\d+)", line)[0]
        cards_in_hand = [encoder.get(card) for card in list(hand)]

        most_repeated_cards = [
            "{}{}".format(cards_in_hand.count(card), card)
            for card in set(cards_in_hand)
        ]
        order = [key[1] for key in sorted(most_repeated_cards, reverse=True) if key[1] != 'A']

        jokerized_cards_in_hand = cards_in_hand

        if 'A' in cards_in_hand and len(order):
            jokerized_cards_in_hand = list(map(lambda x: x.replace('A', order[0]), cards_in_hand))

        counts_of_cards_in_hand = [jokerized_cards_in_hand.count(card) for card in set(jokerized_cards_in_hand)]
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
