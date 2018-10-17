from math import log
from typing import Set, List, Optional, Dict

from nltk import PorterStemmer

from document import Document
from tokenizer import Tokenizer


class TermFrequencyCalculator:
    _stemmer = PorterStemmer()
    _tokenizer = Tokenizer()

    _numbers_of_documents_containing_term: Optional[Dict[str, int]] = {}

    def __init__(self, terms: Set[str], documents):
        self._terms = terms
        self._prepare_terms()

        self._documents: List[Document] = documents
        self._prepare_documents()
        self._calculate_documents_term_frequencies()
        self._calculate_numbers_of_documents_containing_term()
        self._remove_unused_terms()

        self._inverse_document_frequencies = {
            term: self._inverse_document_frequency(term) for term in self._terms
        }

    def _prepare_terms(self):
        self._terms = set([self._stemmer.stem(term) for term in self._terms])

    def _prepare_documents(self):
        for document in self._documents:
            document.tokens = self._tokenizer.tokenize(document.content)
            document.tokens = [self._stemmer.stem(token) for token in document.tokens]

            document.bag_of_words = {term: 0 for term in self._terms}
            for token in document.tokens:
                if token in self._terms:
                    document.bag_of_words[token] += 1

            document.maximum_value_of_bag_of_words = max(document.bag_of_words.values())

    def _calculate_documents_term_frequencies(self):
        for document in self._documents:
            document.term_frequencies = {
                term: document.bag_of_words[term] / document.maximum_value_of_bag_of_words for term in self._terms
            }

    def _calculate_numbers_of_documents_containing_term(self):
        self._numbers_of_documents_containing_term = {
            term: sum([
                1 for document in self._documents if document.bag_of_words[term] > 0
            ]) for term in self._terms
        }

    def _remove_unused_terms(self):
        self._terms = set([term for term in self._terms if self._numbers_of_documents_containing_term[term] > 0])

    def _inverse_document_frequency(self, term):
        number_of_documents = len(self._documents)
        number_of_documents_containing_term = self._numbers_of_documents_containing_term[term]
        return log(number_of_documents / number_of_documents_containing_term, 10)
