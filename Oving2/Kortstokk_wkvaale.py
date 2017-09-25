from sys import stdin
from itertools import repeat


def merge():
    maks = 0
    decks = []
    sortert = [[] for i in range(len(decks))]
    for line in stdin:
        (bokstav, tall) = line.strip().split(':')
        deck = list(zip(map(int, tall.split(',')), repeat(bokstav)))



    while len(decks) > 1:
        stokk1 = decks.pop(0)
        stokk2 = decks.pop(0)
        result = []
        while len(stokk1) > 0 and len(stokk2) > 0:
            if stokk1[0] < stokk2[0]:
                result.append(stokk1.pop(0))
            else:
                result.append(stokk2.pop(0))
        result.extend(stokk1)
        result.extend(stokk2)
        decks.append(result)
    ord = []
    for (tall, bokstav) in decks[0]:
        ord.append(bokstav)
    return ''.join(ord)

print(merge())
