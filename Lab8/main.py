from Controlled_text import *
from First_name import *
from Last_name import *
from Ident_number import *
from Person import *


def main():
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    task_5()


def task_1():
    c = Controlled_text('alala')
    print(c.text)
    c.text = 'Asdas'
    print(c.text)
    try:
        c.text = "alala la"
        print(c.text)
    except ValueError as ex:
        print(ex)


def task_2():
    c = First_name('jakub')
    print(c.text)
    print('Is "Jakub" a male = ', c.is_male())
    print('Is "Iga" a female = ', c.female_name('iga'))
    try:
        c.text = "alalala"
        print(c.text)
    except ValueError as ex:
        print(ex)


def task_3():
    c = Last_name('Szwedowicz')
    print(c.text)
    c.text = 'szwedowicz-gut'
    print(c.text)
    try:
        c.text = "Kowalski Bak"
        print(c.text)
    except ValueError as ex:
        print(ex)


def task_4():
    c = Ident_number('111111107')
    print(c.text)
    try:
        c = Ident_number('111111514')
        print(c.text)
    except ValueError as ex:
        print(ex)


def task_5():
    c = Person.load_from_file()
    for p in c:
        print(p)


if __name__ == '__main__':
    main()