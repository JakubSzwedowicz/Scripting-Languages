from Controlled_text import Controlled_text


class Last_name(Controlled_text):
    def lname(function):
        def wrapper(cls, name: str):
            list_of_names = name.strip().split('-')
            ret = ''
            if len(list_of_names) != 0 and not any(letter.isspace() for letter in list_of_names[0]):
                ret += list_of_names[0].capitalize()
                for n in list_of_names[1:]:
                    ret += '-' + n.capitalize()
                return function(cls, ret)
            else:
                raise ValueError(f'Last name "{name}" must be a single word or words split with "-"')
        return wrapper

    @lname
    def __init__(self, last_name):
        super().__init__(last_name)

    @Controlled_text.text.setter
    @lname
    def text(self, name):
        self._text = name
