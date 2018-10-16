from pathlib import Path


class TermsLoader:

    def __init__(self, file_path: Path):
        self._file_path = file_path

    def load(self):
        with self._file_path.open('r') as file:
            lines = file.readlines()
            terms = []

            for line in lines:
                terms.append(line.replace('\n', ''))

            return terms
