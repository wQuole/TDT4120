liste = [[1,'a'],[2,'b'],[3,'c']]

for (tall,bokstav) in liste:
    lowest = tall % len(liste)
    lowest //= 1


items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))


try:
    import numpy as np

    a = np.arange(15).reshape(3, 5)

    print (a)
except ImportError:
    print("numpy is not installed")
