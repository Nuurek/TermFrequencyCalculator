from pathlib import Path

from nltk import PorterStemmer

from documents_loader import DocumentsLoader
from terms_loader import TermsLoader
from tokenizer import Tokenizer

RESOURCES_PATH = Path.cwd().parent / 'resources'
DOCUMENTS_PATH = RESOURCES_PATH / 'documents.txt'
TERMS_PATH = RESOURCES_PATH / 'keywords.txt'

if __name__ == '__main__':
    documents_loader = DocumentsLoader(DOCUMENTS_PATH)
    documents = documents_loader.load()
    print([document.content for document in documents])

    tokenizer = Tokenizer()
    stemmer = PorterStemmer()
    for document in documents:
        document.tokens = tokenizer.tokenize(document.content)
        document.tokens = [stemmer.stem(token) for token in document.tokens]

    print([document.tokens for document in documents])

    terms_loader = TermsLoader(TERMS_PATH)
    terms = terms_loader.load()
    print([term.original for term in terms])

    for term in terms:
        term.stemmed = stemmer.stem(term.original)

    print([term.stemmed for term in terms])
