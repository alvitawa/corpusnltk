#!/usr/bin/env python3

with open('corpus_fixed.txt', 'r') as f:
    t = f.read().strip()
    words = t.replace('\n', ' ').split(' ')
    print('Sentences: ', len(t.split('\n')))
    print('Words: ', len(words))
    diff_words = set(''.join(filter(str.isalnum, w)) for w in words)
    print('Different Words: ', len(diff_words))
    x = dict()
    for dw in diff_words:x
        x[dw] = words.count(dw)
    print(sorted((a, b) for b,a in x.items()))