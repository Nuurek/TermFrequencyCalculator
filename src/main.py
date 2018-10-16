from pathlib import Path

from documents_loader import DocumentsLoader

RESOURCES_PATH = Path.cwd().parent / 'resources'
DOCUMENTS_PATH = RESOURCES_PATH / 'documents.txt'

if __name__ == '__main__':
    documents_loader = DocumentsLoader(DOCUMENTS_PATH)
    documents = documents_loader.load()
    print(documents)
