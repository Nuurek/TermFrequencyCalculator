from pathlib import Path

from documents_loader import DocumentsLoader
from term_frequency_calculator import TermFrequencyCalculator
from terms_loader import TermsLoader

RESOURCES_PATH = Path.cwd().parent / 'resources'
DOCUMENTS_PATH = RESOURCES_PATH / 'documents.txt'
TERMS_PATH = RESOURCES_PATH / 'keywords.txt'

if __name__ == '__main__':
    terms_loader = TermsLoader(TERMS_PATH)
    terms = terms_loader.load()

    documents_loader = DocumentsLoader(DOCUMENTS_PATH)
    documents = documents_loader.load()

    calculator = TermFrequencyCalculator(terms, documents)

    while True:
        query = input()
        results = calculator.search(query)

        for result in results:
            print(f'{result.similarity}\t{result.document.title}')
        print('\n')
