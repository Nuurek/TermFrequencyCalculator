from pathlib import Path


class DocumentsLoader:

    def __init__(self, file_path: Path):
        self._file_path: Path = file_path

    def load(self, encoding='utf-16'):
        documents = []
        with self._file_path.open('r', encoding=encoding) as file:
            document = ''

            lines = file.readlines()
            for line in lines:
                if line != '\n':
                    document += line
                else:
                    documents.append(document.replace('\n', ' '))
                    document = ''

        return documents
