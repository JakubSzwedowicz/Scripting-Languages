# Author: Jakub Szwedowicz
# Date: 17.03.2022
# e-mail: kuba.szwedowicz@gmail.com

from random import shuffle


def task():
    colors = ['clubs', 'diamonds', 'hearts', 'spades']
    figures = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
               '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    first_part(colors, figures)
    second_part(colors, figures)


def first_part(colors: list, figures: dict) -> None:
    print('========== First part ============')
    cards = prepare_cards(colors, figures)
    shuffle(cards)
    players = [[], []]
    give_cards(cards, players, 5)
    print('First player cards: {0}\nSecond player cards: {1}'.format(players[0], players[1]))


def second_part(colors: list, figures: dict) -> None:
    print('========== Second part ============')
    cards = prepare_cards(colors, figures)
    shuffle(cards)
    print('All the cards: ', cards)

    players = [[], []]
    give_cards(cards, players, 5)

    while min(players, key=len):
        p1_card = players[0].pop()
        p2_card = players[1].pop()
        if p1_card[1] == p2_card[1]:
            players[0].append(p1_card)
            players[1].append(p2_card)
        elif p1_card[1] > p2_card[1]:
            players[0] += [p1_card, p2_card]
        else:
            players[1] += [p1_card, p2_card]

    print('player {0} won'.format(players.index(min(players, key=len))))


def prepare_cards(colors: list, figures: dict) -> list:
    cards = []
    for col in colors:
        for fig, pow in figures.items():
            cards.append([col + ' ' + fig, pow])
    return cards


def give_cards(cards: list, players: list, n_cards: int) -> None:
    for p in players:
        for _ in range(0, n_cards):
            p.append(cards.pop())
