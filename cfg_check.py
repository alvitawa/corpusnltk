#!/usr/bin/env python3

import nltk
from nltk.grammar import FeatureGrammar
from nltk.parse import BottomUpLeftCornerChartParser

from grammar_load import grammar, corpus


# Function that works for multiple types of parsers (You are free to use something else if you want.)
def check_sentence(parser, sentence):
    if isinstance(sentence, str):
        sentence = nltk.word_tokenize(sentence)
    tree_found = False
    results = parser.parse(sentence)
    for tree in results:
        tree_found = True
        # print(tree)
    return tree_found

parser = BottomUpLeftCornerChartParser(grammar)

succ = 0
fail = 0
for sentence in (corpus.split('\n')):
    # print('try' + sentence)
    if not check_sentence(parser, sentence):
        print('Nomatch \'%s\'' % sentence)
        fail += 1
    else:
        # print('succ \'%s\'' % sentence)
        succ += 1

print('success: %s; failure: %s;' % (succ, fail))