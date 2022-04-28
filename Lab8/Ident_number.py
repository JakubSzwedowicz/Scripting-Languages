from Controlled_text import Controlled_text


class Ident_number(Controlled_text):
    _modulo = 97

    def __init__(self, number: str):
        super().__init__(number)
        if not Ident_number.is_valid_ident_numer(self.text):
            raise ValueError(f'Number "{number}" is not 9 chars long or number[:7] % 97 != number [7:]')

    @staticmethod
    def is_valid_ident_numer(number: str) -> bool:
        try:
            controlled = Controlled_text(number)
            if len(controlled.text) == 9:
                _sum = sum(map(int, controlled.text[:7]))
                crc = int(controlled.text[7:])
                return _sum % Ident_number._modulo == crc
        except ValueError:
            return False
