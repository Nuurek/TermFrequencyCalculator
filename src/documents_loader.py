from pathlib import Path
from typing import List

from document import Document


class DocumentsLoader:

    def __init__(self, file_path: Path):
        self._file_path: Path = file_path

    def load(self, encoding='utf-16') -> List[Document]:
        documents = []
        with self._file_path.open('r', encoding=encoding) as file:
            title = ''
            content = ''

            lines = file.readlines()
            for line in lines:
                line = line.replace('\n', ' ')
                if line != ' ':
                    if content == '':
                        title = line

                    content += line
                else:
                    if content != '':
                        document = Document(title, content)
                        documents.append(document)
                    title = ''
                    content = ''

        return documents
