from Controlled_text import Controlled_text


class First_name(Controlled_text):
    _are_names_loaded = False
    female = 'Kobiety'
    male = 'Mężczyźni'
    _loaded_names = {female: [], male: []}

    def name(func):
        def wrapper(cls, name: str):
            return func(cls, name.capitalize())
        return wrapper

    @name
    def __init__(self, name: str):
        First_name._load_names()
        super().__init__(name)

    @Controlled_text.text.setter
    @name
    def text(self, name):
        if not First_name._is_valid_name(name):
            raise ValueError(f'"{name}" is not a valid attribute for First_name')
        self._text = name

    def is_male(self):
        return self.text in self._loaded_names[First_name.male]

    def is_female(self):
        return self.text in self._loaded_names[First_name.female]

    @name
    def male_name(self, name: str):
        return name in self._loaded_names[First_name.male]

    @name
    def female_name(self, name: str):
        return name in self._loaded_names[First_name.female]

    @classmethod
    @name
    def _is_valid_name(cls, name) -> bool:
        if not First_name._are_names_loaded:
            First_name._load_names()
        for values in cls._loaded_names.values():
            if name in values:
                return True
        return False

    @staticmethod
    def _load_names(filename: str = 'Popularne imiona.txt') -> None:
        if First_name._are_names_loaded:
            return

        curr_gender = First_name.male
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    if line == First_name.female:
                        curr_gender = First_name.female
                    elif line == First_name.male:
                        curr_gender = First_name.male
                    else:
                        First_name._loaded_names[curr_gender].append(line)
        First_name._are_names_loaded = True


