import numpy as np

if 0:
    # Check if a number is prime
    def is_prime(x):
        for d in range (2,x//2):
            if x%d == 0:
                return 0
        return 1

    print(is_prime(30))

    # Sort alphabetically the words from text.txt
    file = open("text.txt","r")
    words = file.read().split(" ")
    for i in range(0, len(words)):
        try:
            x = words[i].split(".")
            words[i] = x[0]
        except:
            pass
        words[i] = words[i].lower()

    words.sort()
    print(words)

    # Matrix multiplication
    matrixA = [[1,2,3,4],
               [11,12,13,14],
               [21,22,23,24]]
    matrixB = [[2,-5, 7, -10]]

    matrixAB = []
    for i in range(len(matrixA[0])-1):
        s = 0
        for j in range(len(matrixB[0])-1):
            s += matrixA[i][j] * matrixB[0][j]
        matrixAB.append(s)

    print(matrixAB)

# Numpy exercises
# Exercise 1
# --a)--
if 0:
    matrix = np.array([[1,2,3,4],
                       [11,12,13,14],
                       [21,22,23,24]])
    vector = np.array([2,-5, 7, -10])
    print(matrix[:-1, 2:])

# --b)--
    print(vector[2:])

# Exercise 2
if 0:
    array1 = np.random.randint(2, size=10)
    array2 = np.random.randint(2, size=10)

    # --a)--
    sum1 = array1.sum()
    sum2 = array2.sum()
    if sum1 > sum2:
        print("First array")
    elif sum1 < sum2:
        print("Second array")
    else:
        print("Nothing")

    # --b)--
    print(array1)
    print(array2)
    print(array1 + array2)
    print(array1 * array2)
    print(np.dot(array1,array2))
    # --c)--
    print(np.sqrt(array1))
    print(np.sqrt(array2))

# Exercise 3
a1 = np.random.randint(0, 2, (5, 3))
print(a1)
trans = np.transpose(a1)
print(trans)