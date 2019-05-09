#!/usr/bin/env python3

from grammar_load import grammar
from generate import generate_phrase

print(list(generate_phrase(grammar)))
    