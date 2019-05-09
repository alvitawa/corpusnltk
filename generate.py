from random import choices

def generate_phrase(grammar, prod = None):
    if not prod:
        prod = grammar.start()
    if prod in grammar._lhs_index:
        # Non-terminals
        derivations = grammar._lhs_index[prod]
        try:
            probabilities = [d.prob() for d in derivations]
        except AttributeError:
            probabilities = None
        derivation = choices(derivations, probabilities)[0]           
        for d in derivation._rhs:            
            yield from generate_phrase(grammar, d)
    elif prod in grammar._rhs_index:
        # Terminals
        yield str(prod)
        
def generate_corpus(grammar, prod = None):
    yield list(generate_phrase(grammar, prod))