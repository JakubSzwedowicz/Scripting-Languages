# Author: Jakub Szwedowicz
# Date: 16.03.2022
# e-mail: kuba.szwedowicz@gmail.com
from random import randint


def task():
    results = [0, 0]
    for turn in range(0, 1):
        for throw in range(1, 5):
            results[turn] += randint(1, 6)

    best_res = max(results)
    better_turns = [i for i, j in enumerate(results) if j == best_res]

    print('The best result was {0} in throws {1}'.format(best_res, better_turns))
