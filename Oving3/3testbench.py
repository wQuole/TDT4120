def test(A):
    len_A = len(A)
    modulus = 10
    div = 1
    while True:
        new_list = [[] for i in range(len_A)]
        for value in A:
           # print("Value:",value,"______________")
            least_digit = value % modulus
           # print("Least:",least_digit)
            least_digit //= div
           # print("Least2::::::",least_digit)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_A:
            return new_list[0]

        A = []
        list_append = A.append
        for x in new_list:
            for y in x:
                list_append(y)
#test(A)

#print(test(A))


def sort_list(A):
    # NOTICE: The sorted list must be returned.
    len_A = len(A)
    modulus = 10
    div = 1
    while True:
        new_list = [[] for i in range(10)]
        for value in A:
            least_digit = value % modulus
            least_digit //= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_A:
            return new_list[0]

        A = []
        list_append = A.append
        for x in new_list:
            for y in x:
                list_append(y)

A = [1,12,3,9,2,7,1]

print(sort_list(A))


