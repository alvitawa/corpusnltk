#!/usr/bin/env python3


with open('CFG_altered.txt', 'r') as config_file:

    t = config_file.read()

    for s in t.split('\n'):
        if "'" not in s:
            print(s)