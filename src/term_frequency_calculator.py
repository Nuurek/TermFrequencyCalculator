from math import log, sqrt
from typing import Set, List, Optional, Dict

from nltk import PorterStemmer

from document import Document
from tokenizer import Tokenizer


class SearchResult:

    def __init__(self, similarity: float, document: Document):
        self.similarity = similarity
        self.document = document

    def __gt__(self, other):
        return self.similarity > other.similarity

    def __lt__(self, other):
        return self.similarity < other.similarity


class TermFrequencyCalculator:
    _stemmer = PorterStemmer()
    _tokenizer = Tokenizer()

    _numbers_of_documents_containing_term: Optional[Dict[str, int]] = None
    _inverse_document_frequencies: Optional[Dict[str, float]] = None

    def __init__(self, terms: Set[str], documents):
        self._terms = terms
        self._prepare_terms()

        self._documents: List[Document] = documents
        self._prepare_documents()

        self._calculate_documents_bag_of_words()
        self._calculate_numbers_of_documents_containing_term()
        self._remove_unused_terms()
        self._calculate_documents_term_frequencies()

        self._calculate_terms_inverse_document_frequencies()
        self._calculate_documents_inverse_term_frequencies()
        self._calculate_documents_vector_length()

    def search(self, query) -> List[SearchResult]:
        query_document = Document(query, query)
        self._prepare_document(query_document)
        self._calculate_document_bag_of_words(query_document)
        self._calculate_document_term_frequencies(query_document)
        self._calculate_document_inverse_term_frequencies(query_document)
        self._calculate_document_vector_length(query_document)

        results = []
        for document in self._documents:
            similarity = self._calculate_documents_similarity(document, query_document)
            results.append(SearchResult(similarity, document))

        results.sort(reverse=True)

        return results

    def _prepare_terms(self):
        self._terms = set([self._stemmer.stem(term) for term in self._terms])

    def _prepare_documents(self):
        for document in self._documents:
            self._prepare_document(document)

    def _prepare_document(self, document: Document):
        document.tokens = self._tokenizer.tokenize(document.content)
        document.tokens = [self._stemmer.stem(token) for token in document.tokens]

    def _calculate_documents_bag_of_words(self):
        for document in self._documents:
            self._calculate_document_bag_of_words(document)

    def _calculate_document_bag_of_words(self, document: Document):
        document.bag_of_words = {term: 0 for term in self._terms}
        for token in document.tokens:
            if token in self._terms:
                document.bag_of_words[token] += 1

        document.maximum_value_of_bag_of_words = max(document.bag_of_words.values())

    def _calculate_numbers_of_documents_containing_term(self):
        self._numbers_of_documents_containing_term = {
            term: sum([
                1 for document in self._documents if document.bag_of_words[term] > 0
            ]) for term in self._terms
        }

    def _remove_unused_terms(self):
        self._terms = set([term for term in self._terms if self._numbers_of_documents_containing_term[term] > 0])

        for document in self._documents:
            document.bag_of_words = {
                term: document.bag_of_words[term] for term in self._terms
            }

    def _calculate_documents_term_frequencies(self):
        for document in self._documents:
            self._calculate_document_term_frequencies(document)

    def _calculate_document_term_frequencies(self, document: Document):
        document.term_frequencies = {
            term: document.bag_of_words[term] / document.maximum_value_of_bag_of_words for term in self._terms
        }

    def _calculate_terms_inverse_document_frequencies(self):
        self._inverse_document_frequencies = {
            term: self._inverse_document_frequency(term) for term in self._terms
        }

    def _inverse_document_frequency(self, term):
        number_of_documents = len(self._documents)
        number_of_documents_containing_term = self._numbers_of_documents_containing_term[term]
        return log(number_of_documents / number_of_documents_containing_term, 10)

    def _calculate_documents_inverse_term_frequencies(self):
        for document in self._documents:
            document.inverse_term_frequencies = {
                term: document.term_frequencies[term] * self._inverse_document_frequencies[term] for term in self._terms
            }

    def _calculate_document_inverse_term_frequencies(self, document: Document):
        document.inverse_term_frequencies = {
            term: document.term_frequencies[term] * self._inverse_document_frequencies[term] for term in self._terms
        }

    def _calculate_documents_vector_length(self):
        for document in self._documents:
            self._calculate_document_vector_length(document)

    @staticmethod
    def _calculate_document_vector_length(document: Document):
        document.vector_length = sqrt(sum([
            pow(frequency, 2) for frequency in document.inverse_term_frequencies.values()
        ]))

    def _calculate_documents_similarity(self, first: Document, second: Document):
        numerator = 0
        for term in self._terms:
            numerator += first.inverse_term_frequencies[term] * second.inverse_term_frequencies[term]

        denominator = first.vector_length * second.vector_length

        return numerator / denominator
