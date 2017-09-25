from sys import stdin


class Dynamitt:
    value = None
    next = None

    def __init__(self, value):
        self.value = value
        self.next = None


def search(tnt):
    maks = 0
    while tnt != None:
        if tnt.value > maks:
            maks = tnt.value
        tnt = tnt.next
    return maks

def main():
    # reading from stdin and creating a linked list
    first = None
    last = None
    for line in stdin:
        penultimate = last
        last = Dynamitt(int(line))
        if first is None:
            first = last
        else:
            penultimate.next = last

    # searching and printing out the result
    print(search(first))


if __name__ == "__main__":
    main()