from pathlib import Path

from term import Term


class TermsLoader:

    def __init__(self, file_path: Path):
        self._file_path = file_path

    def load(self):
        with self._file_path.open('r') as file:
            lines = file.readlines()
            terms = []

            for line in lines:
                line = line.replace('\n', '')
                term = Term(line)
                terms.append(term)

            return terms
