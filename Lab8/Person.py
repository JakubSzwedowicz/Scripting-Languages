from First_name import First_name
from Last_name import Last_name
from Ident_number import Ident_number


class Person:
    def __init__(self, first_name: First_name, last_name: Last_name, ident_number: Ident_number):
        self._first_name = First_name(first_name)
        self._last_name = Last_name(last_name)
        self._ident_number = Ident_number(ident_number)

    def __repr__(self) -> str:
        return f'{self._first_name.text} {self._last_name.text} {self._ident_number.text}'

    @staticmethod
    def load_from_file(file_name: str = 'People.txt') -> list:
        result = []
        with open(file_name, 'r') as f:
            for line in f:
                fname, lname, number = line.split()
                try:
                    result.append(Person(fname, lname, number))
                except Exception as ex:
                    print(ex)
        return result
