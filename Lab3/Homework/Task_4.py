# Author: Jakub Szwedowicz
# Date: 17.03.2022
# e-mail: kuba.szwedowicz@gmail.com
import random


def task():
    n_lotto_numbers = 6
    print('Lotto winning numbers:', random.sample(range(0, 50), n_lotto_numbers))
