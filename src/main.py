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
    print(documents)

    tokenizer = Tokenizer()
    tokenized_documents = [tokenizer.tokenize(document) for document in documents]

    stemmer = PorterStemmer()
    stemmed_documents = [[stemmer.stem(token) for token in document] for document in tokenized_documents]
    print(stemmed_documents)

    terms_loader = TermsLoader(TERMS_PATH)
    terms = terms_loader.load()
    print(terms)

    stemmed_terms = [stemmer.stem(term) for term in terms]
    print(stemmed_terms)
