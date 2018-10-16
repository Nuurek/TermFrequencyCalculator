from typing import Optional, List


class Document:
    title: str
    content: str
    tokens: Optional[List[str]]

    def __init__(self, title, content):
        self.title = title
        self.content = content
