class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    rot = Node()
    for (word,pos) in ordliste:
        node = rot
        for char in word:
            if char in node.barn:
                node = node.barn[char]
            else:
                node.barn[char] = Node()
                node = node.barn[char]
        node.posi.append(pos)
    return rot

def posisjoner(word,indeks,node,length):
    char = word[indeks]
    if char in node.barn:
        if indeks == length:
            return node.barn[char].posi
        return posisjoner(word, indeks +1, node.barn[char], length)
    elif char == '?':
        liste = []
        for k in node.barn.values():
            if indeks == length:
                liste += k.posi
            else:
                liste += (posisjoner(word, indeks + 1, k, length))
        return liste
    else:
        return []

def main():
    from sys import stdin
    word = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in word:
        ordliste.append((o, pos))
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print("%s:" % sokeord, end='')
        length = len(sokeord) - 1
        posi = posisjoner(sokeord, 0, toppnode, length)
        posi.sort()
        for p in posi:
            print(" %s" % p, end='')
        print()

main()