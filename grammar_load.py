
import nltk
from nltk import PCFG
from nltk.grammar import FeatureGrammar
from nltk.parse import BottomUpLeftCornerChartParser

with open('lexicon.txt', 'r') as lexicon_file, \
     open('corpus_fixed.txt', 'r') as corpus_file, \
     open('CFG_altered.txt', 'r') as config_file:

    lexicon_text = lexicon_file.read()
    corpus = corpus_file.read()
    cfg_text = config_file.read()

    cfg_full = 'start -> ROOT [1.0] \n' + cfg_text #+ '\n' + lexicon_text
    # print(cfg_full)

    grammar = PCFG.fromstring(cfg_full)
    # grammar._start = 'S'