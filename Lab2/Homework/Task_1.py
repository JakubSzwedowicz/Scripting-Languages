# Author: Jakub Szwedowicz
# Date: 16.03.2022
# e-mail: kuba.szwedowicz@gmail.com

import math


def task():
    full_angle = 360
    angle_to_radians_divider = math.pi / 180

    angles = [360, 90, 45]
    angles_to_radians = [x * angle_to_radians_divider for x in angles]

    header = ['Degress', 'math.radians', 'custom_radians']

    print('{:<8} {:<15} {:<15}'.format(*header))
    for i in range(0, 2):
        print('{:<8} {:<15.5f} {:<15.5f}'.format(angles[i], math.radians(angles[i]), angles_to_radians[i]))


