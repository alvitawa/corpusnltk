#!/usr/bin/env python3

def parse(tree):
    tree = tree.strip()
    if tree.count('(') == 0 and tree.count(' ') == 0:
        return [tree]
    parts_ixs = []
    depth = 0
    for i, c in enumerate(tree):
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        elif c == ' ' and depth == 1:
            parts_ixs.append(i)
    parts = []
    prev_ix = 0
    for part_ix in parts_ixs:
        part = tree[prev_ix+1:part_ix]
        prev_ix = part_ix
        parts.append(part)
    parts.append(tree[prev_ix+1:-1])
    # print(parts, end='\n\n')
    parsed_parts = list(parse(part) for part in parts[1:])
    # print([parts[0], parsed_parts])
    return [parts[0], *parsed_parts]

def rules(parsed):
    if len(parsed) == 1:
        return set()

    # print(parsed)
    if len(parsed[1]) == 1:
        new_rules = set([(parsed[0], f'\'{parsed[1][0]}\'')])
        # print(parsed, new_rules)
    else:
        new_rules = set([(parsed[0] ,' '.join(p[0] for p in parsed[1:]))])
    
    # print(parsed)
    for sub in parsed[1:]:
        # print('==---SUB: ', sub)
        new_rules.update(rules(sub))

    return new_rules

with open('corenlp.txt', 'r') as inpt, open('CFG_auto.txt', 'w') as out:
    file_text = inpt.read()
    ruleset = set()
    for treestr in file_text.split('\n'):
        parsed = parse(treestr)
        new_rules = rules(parsed)
        ruleset.update(new_rules)
   
    for rule in sorted(ruleset):
        head = rule[0]
        tail = rule[1].split(' ')
        out.write(head + ' -> ' + ' '.join(tail) + '\n')

    # out.write('\n'.join(ruleset))

['ROOT', ['S', ['NP', ['PRP', ['it']]], ['VP', ['VBD', ['bit']], ['NP', ['PRP', ['him']]]], ['.', ['.)']]]]
