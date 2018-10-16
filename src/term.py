from typing import Optional


class Term:
    original: str
    stemmed: Optional[str]

    def __init__(self, term):
        self.original = term
