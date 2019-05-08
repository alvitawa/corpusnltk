#!/usr/bin/env python3

import nltk
from nltk import CFG
from nltk.grammar import FeatureGrammar
from nltk.parse import ShiftReduceParser

# Function that works for multiple types of parsers (You are free to use something else if you want.)
def check_sentence(parser, sentence):
    if isinstance(sentence, str):
        sentence = nltk.word_tokenize(sentence)
    tree_found = False
    results = parser.parse(sentence)
    for tree in results:
        tree_found = True
        print(tree)
    return tree_found

# TODO!!: lexicon_fixed.txt
with open('lexicon_fixed.txt', 'r') as lexicon_file, \
     open('out.txt', 'r') as corpus_file, \
     open('CFG.txt', 'r') as config_file, \
     open('generated.txt', 'w') as gen_out:

    lexicon_text = lexicon_file.read()
    corpus = corpus_file.read()
    cfg_text = config_file.read()

    cfg_full = cfg_text + '\n' + lexicon_text
    # cfg_full = """
    #     S -> CC
    #     CC -> 'and'
    # """

    # print(cfg_full)

    cfg = CFG.fromstring(cfg_full)
    parser = nltk.parse.chart.BottomUpLeftCornerChartParser(cfg)
    
    succ = 0
    fail = 0
    for sentence in corpus.split('\n')[:1]:
        # print('try' + sentence)
        if not check_sentence(parser, sentence):
            print('Nomatch \'%s\'\n\n' % sentence)
            fail += 1
        else:
            print('succ')
            succ += 1

    print('success: %s; failure: %s;' % (succ, fail))