from typing import Optional, List, Dict


class Document:
    title: str
    content: str
    tokens: Optional[List[str]]
    bag_of_words: Optional[Dict[str, int]]
    maximum_value_of_bag_of_words: Optional[int]
    term_frequencies: Optional[Dict[str, float]]

    def __init__(self, title, content):
        self.title = title
        self.content = content
