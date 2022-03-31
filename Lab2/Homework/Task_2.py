# Author: Jakub Szwedowicz
# Date: 16.03.2022
# e-mail: kuba.szwedowicz@gmail.com
import random
from random import shuffle


def task():
    countries = ['Uruguay', 'Russia', 'Saudi Arabia', 'Egypt', 'Spain', 'Portugal', 'Iran', 'Morocco', 'France',
                 'Denmark', 'Peru', 'Australia', 'Croatia', 'Argentina', 'Nigeria', 'Iceland', 'Brazil', 'Switzerland',
                 'Serbia', 'Costa Rica', 'Sweden', 'Mexico',
                 'Korea Republic', 'Germany', 'Belgium', 'England', 'Tunisia', 'Panama', 'Colombia', 'Japan', 'Senegal',
                 'Poland']

    shuffle(countries)

    n_random_countries = 8
    random_countries = [countries[i] for i in random.sample(range(0, len(countries)), n_random_countries)]
    print(random_countries)
