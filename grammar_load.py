
import nltk
from nltk import CFG
from nltk.grammar import FeatureGrammar
from nltk.parse import BottomUpLeftCornerChartParser

with open('lexicon.txt', 'r') as lexicon_file, \
     open('corpus_fixed.txt', 'r') as corpus_file, \
     open('CFG_auto.txt', 'r') as config_file:

    lexicon_text = lexicon_file.read()
    corpus = corpus_file.read()
    cfg_text = config_file.read()

    cfg_full = cfg_text + '\n' + lexicon_text

    grammar = CFG.fromstring('start -> ROOT\n' + cfg_full)
    # grammar._start = 'S'