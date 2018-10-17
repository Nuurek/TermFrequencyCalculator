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
    print(terms)

    documents_loader = DocumentsLoader(DOCUMENTS_PATH)
    documents = documents_loader.load()
    print([document.content for document in documents])

    calculator = TermFrequencyCalculator(terms, documents)

    print(calculator._terms)
    print([document.tokens for document in calculator._documents])
    print([document.bag_of_words for document in calculator._documents])
    print([document.term_frequencies for document in calculator._documents])
    print(calculator._inverse_document_frequencies)
