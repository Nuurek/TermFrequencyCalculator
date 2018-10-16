class Tokenizer:
    separators = ['.', ',', ';', ':', '&', '|', '(', ')', '!']

    def tokenize(self, sentence: str):
        new_sentence = ''

        for char in sentence:
            if char not in self.separators:
                new_sentence += char

        tokens = new_sentence.split(' ')
        tokens = [token.lower() for token in tokens if token != '']

        return tokens
