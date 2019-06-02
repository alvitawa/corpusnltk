#!/usr/bin/env python3

from grammar_load import grammar
from generate import generate_phrase

# print(' '.join(generate_phrase(grammar)))
    
with open('generated.txt', 'w') as gen_out:
    for i in range(50):
        while True:
            try:
                s = ' '.join(generate_phrase(grammar))
                gen_out.write(s + '\n\n')
                print(s)
                break
            except:
                continue