#!/usr/bin/env python3

with open('in.txt', 'r') as in_file, open('out.txt', 'w') as out_file:
    content = in_file.read()
    text = ''
    for sentence in content.split('.'):
        if sentence.count("\"") < 1:
            text += sentence + '.'
        if len(text.split(' ')) > 1000:
            break
    out_file.write(text)
    print('Words: ~%s' % len(text.split(' ')))



    
