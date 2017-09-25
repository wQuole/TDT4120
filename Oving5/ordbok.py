#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    toppnode = Node()
    for (ord,posisjon) in ordliste:
        node = toppnode
        for char in ord:
            if not char in node.barn:
                node.barn[char] = Node()
            node.posi.append(posisjon)
        return toppnode

def posisjoner(ord, indeks, node):
    return


def main():
    try:
        ord = stdin.readline().split()
        print("Ord:",ord)
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            print("Ordliste:",ordliste)
            pos += len(o) + 1
            print("Pos:",pos)
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("Sokeord: ",sokeord)
            print("%s:" % sokeord, end='')
            #posi = posisjoner(sokeord, 0, toppnode)
            #posi.sort()
            #for p in posi:
            #    print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()

