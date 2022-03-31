# Author: Jakub Szwedowicz
# Date: 17.03.2022
# e-mail: kuba.szwedowicz@gmail.com
import os


def task():
    str_data = ''
    list_data = []

    str_data = input('Enter the url address of website: ')

    str_data = 'ExampleFile.txt'
    print('========= Reading the basic file ==========')
    with open(str_data, 'r') as file:
        for line in file:
            print(line)

    print('========= Appending to the basic file ==========')
    with open(str_data, 'a') as file:
        file.write('C++ es numero uno\n')

    with open(str_data, 'r') as file:
        for line in file:
            print(line)

    print('========= Overwriting the basic file ==========')
    with open(str_data, 'w') as file:
        file.write('Some random sentence\n')

    with open(str_data, 'r') as file:
        for line in file:
            print(line)
