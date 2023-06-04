#!/usr/bin/en python3

import string


def file_to_string(query_filename):
    with open(query_filename) as f:
        query_lines = f.readlines()
    return query_lines


def preprocess_string(query_contents):
    content = ""
    for line in query_contents:
        if not line.strip().startswith("-- "):
            # ignore the comments
            content = content + line.strip() + " "

    content = content.translate(str.maketrans({key: " {0} ".format(key) for key in string.punctuation}))
    return content


def query_to_tokens(query_contents):
    words = query_contents.split()
    words = [word.strip().upper() for word in words]
    return words


def count_token_matches(haystack, needles):
    occurrences = 0
    for hay in haystack:
        if hay in needles:
            occurrences = occurrences + 1
    
    return occurrences



class TokenCounter:
    def __init__(self, tokens_filename):
        with open(tokens_filename) as f:
            tokens = f.readlines()
        self.tokens = set([token.strip() for token in tokens])

    def count_tokens(self, query_filename):
        return count_token_matches(\
            query_to_tokens(preprocess_string(file_to_string(query_filename))), \
            self.tokens)



if __name__ == '__main__':
    token_counter = TokenCounter("sql-tokens.txt")
    assert token_counter.count_tokens("sql-tokens.txt") == 13
