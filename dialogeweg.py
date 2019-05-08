#!/usr/bin/env python3

with open('in.txt', 'r') as in_file, open('out.txt', 'w') as out_file:
    content = in_file.read()
    print('Original: ~%s' % len(content.split(' ')))
    text = ''
    for sentence in content.split('.'):
        if '\'' in sentence:
            continue
        if '\"' in sentence:
            continue
        if '-' in sentence: 
            continue
        if '.' in sentence:
            continue
        if '(' in sentence or ')' in sentence:
            continue
        # no_commas = ''.join(sentence.split(','))
        stripped = sentence.strip()
        if stripped == '':
            continue
        text += stripped + '.\n' #no_commas + '. '
        if len(text.split(' ')) > 1000:
            break
    out_file.write(text)
    print('Words: ~%s' % len(text.split(' ')))



    
