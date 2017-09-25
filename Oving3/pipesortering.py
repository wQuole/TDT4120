from sys import stdin

#Quick Sort
def sort_list(A):
    length = len(A)
    if length <=1:
        return A
    else:
        pivot = A.pop(int(length/2))
        less, more = [], []
        for x in A:
            if x<=pivot:
                less.append(x)
            else:
                more.append(x)
        return sort_list(less) + [pivot] + sort_list(more)
"""
def sort_list(A):
    if A == []:
        return []
    else:
        pivot = A[0]
        lesser = sort_list([x for x in A[1:] if x < pivot])
        greater = sort_list([x for x in A[1:] if x >= pivot])
        return lesser + [pivot] + greater
"""

def find(A, lower, upper):
    index_lower = binary_search(A, lower)
    index_upper = binary_search(A, upper)
    if A[index_lower] > lower and lower != 0:
        index_lower -= 1
    if A[index_upper] < upper and index_upper != len(A)-1:
        index_upper += 1
    return [A[index_lower], A[index_upper]]


def binary_search(A, t):
    lower = 0
    upper = len(A) - 1
    while lower < upper:  # use < instead of <=
        mid = lower + (upper - lower) // 2
        value = A[mid]
        if t == value:
            return mid
        elif t > value:
            if lower == mid:
                break  #voila
            lower = mid
        elif t < value:
            upper = mid
    return mid

def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()