#Implementasjon uten Class Node

def bygg(ordliste):
    rot = ({},[])
    for (word,pos) in ordliste:
        node = rot
        for char in word:
            if char in node[0]:
                node = node[0][char]
            else:
                node[0][char] = ({},[])
                node = node[0][char]
        node[1].append(pos)
    return rot

def posisjoner(word,indeks,node,length):
    char = word[indeks]
    if char in node[0]:
        if indeks == length:
            return node[0][char][1]
        return posisjoner(word, indeks +1, node[0][char], length)
    elif char == '?':
        liste = []
        for k in node[0].values():
            if indeks == length:
                liste.extend(k[1])
            else:
                liste.extend(posisjoner(word, indeks + 1, k, length))
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