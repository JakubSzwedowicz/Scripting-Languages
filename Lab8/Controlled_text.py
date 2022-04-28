class Controlled_text:
    class Text:
        def __init__(self, f):
            self._f = f

        def __call__(self, *args: str, **kwargs):
            for text in args[1:]:
                if type(text) != str or not text.isprintable() or any(letter.isspace() for letter in text):
                    raise ValueError(f'Passed text "{text}" is not printable or contains a whitespace')
            self._f(*args, **kwargs)

    def __init__(self, text: str):
        if type(text) != str:
            raise TypeError('Controlled_text attribute must be of type str()')
        self.text = text

    @property
    def text(self):
        return self._text

    @text.setter
    @Text
    def text(self, text: str):
        self._text = text

    def __ge__(self, other):
        return self._text > other._text

    def __gt__(self, other):
        return self._text >= other._text

    def __le__(self, other):
        return self._text < other._text

    def __lt__(self, other):
        return self._text <= other._text

    def __eq__(self, other):
        return self._text == other._text



