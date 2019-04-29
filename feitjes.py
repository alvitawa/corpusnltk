f = open('corpus.txt')
raw = f.read()
tokens = word_tokenize(raw)
x = raw.split()
wordcheck = []
for word in x:
        if word.isalpha():
            wordcheck.append(word.lower())
        elif "," in word:
            xword = word.split(",")
            wordcheck.append(xword[0].lower())
        elif "." in word:
            xword = word.split(".")
            wordcheck.append(xword[0].lower())
x = wordcheck
lengthx = len(x)
y = raw.split(".")
lengthy = len(y)
print("aantal woorden is",lengthx)
print("aantal zinnen is",lengthy)
words = set()
for word in x:
    words.add(word)
print("aantal verschillende woorden", len(words))
occ = {}
for word in x:
    if word not in occ:
        occ[word]=1
    else:
        occ[word] += 1
getal = 0
for z,n in occ.items():
    if n == 1:
        getal += 1
        hapaxes.append(z)
number = 0
for w in sorted(occ, key=occ.get, reverse=True):
    if occ[w] != 1:
        number += 1
gemiddelde = 0
for word in x:
    for c in word:
        gemiddelde += 1
print("gemiddelde aantal letters:", gemiddelde/len(x))
print("zoveel veelvoorkomende woorden:", number)
print("zoveel hapaxes:", getal)
