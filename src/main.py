from pathlib import Path

from documents_loader import DocumentsLoader
from terms_loader import TermsLoader

RESOURCES_PATH = Path.cwd().parent / 'resources'
DOCUMENTS_PATH = RESOURCES_PATH / 'documents.txt'
TERMS_PATH = RESOURCES_PATH / 'keywords.txt'

if __name__ == '__main__':
    documents_loader = DocumentsLoader(DOCUMENTS_PATH)
    documents = documents_loader.load()
    print(documents)

    terms_loader = TermsLoader(TERMS_PATH)
    terms = terms_loader.load()
    print(terms)
