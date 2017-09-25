#!/usr/bin/python3
from sys import stdin
# from string import ascii_lowercase as chars
from collections import deque

BASE = 26

def flexradix(A, siffer):
    if len(A) <= 1: return A

    f = []
    h = [[] for _ in range(BASE)]

    for s in A:
        if siffer >= len(s):
            f.append(s)
        else:
            h[ord(s[siffer]) - ord('a')].append(s)

    h = [flexradix(ha, siffer + 1) for ha in h]

    return f + [b for he in h for b in he]


def main():
    d = int(stdin.readline())
    print("Lengstre string: "+str(d))
    strings = []
    #while not d.isdigit():
    for line in stdin:
        strings.append(line.rstrip())
    A = flexradix(strings, 0)
    for string in A:
        print(string)


if __name__ == "__main__":
    main()