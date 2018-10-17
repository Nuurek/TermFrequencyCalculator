from pathlib import Path
from typing import Set


class TermsLoader:

    def __init__(self, file_path: Path):
        self._file_path = file_path

    def load(self) -> Set[str]:
        with self._file_path.open('r') as file:
            lines = file.readlines()
            terms = set()

            for line in lines:
                term = line.replace('\n', '')
                terms.add(term)

            return terms
