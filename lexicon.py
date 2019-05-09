#!/usr/bin/env python3

import nltk

with open('out.txt', 'r') as in_file, open('lexicon.txt', 'w') as lexicon_file:
    corpus = in_file.read()
    atoms = nltk.word_tokenize(corpus)
    lexicon = set(nltk.pos_tag(atoms))

    str_lexicon = ''
    for pair in sorted(tuple(reversed(pair)) for pair in lexicon):
        str_lexicon += ' -> \''.join(pair) + '\'\n'
    lexicon_file.write(str_lexicon)