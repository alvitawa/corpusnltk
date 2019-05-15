#!/usr/bin/env python3

from grammar_load import grammar
from generate import generate_phrase

print(' '.join(generate_phrase(grammar)))
    
with open('generated.txt', 'w') as gen_out:
    pass