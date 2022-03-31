# Author: Jakub Szwedowicz
# Date: 10.03.2022
# e-mail: kuba.szwedowicz@gmail.com

class JSOS:
    def __init__(self):
        self._firstnames = []
        self._surnames = []
        self._full_name = []
        self._emails = []
        self._domain = '@pwr.edu.pl'

    def add_new(self) -> None:
        print('Hello!')
        firstname = input('Please input your firstname: ')
        surname = input('Please input your surname: ')
        self._update_with_new(firstname, surname)

        print('Your email is {0:s}'.format(self._emails[-1]))

    def _update_with_new(self, firstname: str, surname: str) -> None:
        self._firstnames.append(firstname)
        self._surnames.append(surname)
        self._full_name.append(firstname + ' ' + surname)
        self._emails.append(firstname.lower() + '.' + surname.lower() + self._domain)
