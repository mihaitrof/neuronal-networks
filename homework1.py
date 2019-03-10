import re
import numpy as np

def readFile(fileName = "data.txt"):
    file = open(fileName,"r")
    words = re.split("[+ \n =]", file.read())
    return words

# Python
def convertEcuationsToMatrix():
    words = readFile()
    coef = ['a', 'b', 'c']
    line = []
    r    = []
    count = 0
    line.append([])
    for i in words:
        for j in coef:
            if j in i:
                el = i.split(j)[0]
                if '-' in el:
                    line[count].append(int(el[el.find("-")+1]) * (-1))
                elif el != '':
                    line[count].append(int(el))
                else:
                    line[count].append(1)

        if len(line[count]) == 0:
            r.append(int(i))
        if len(line[count])%len(coef) == 0:
            count += 1
            line.append([])
    line = [x for x in line if x != []]
    return line, r

def det(A):
    A.append(A[0])
    A.append(A[1])
    plus  = 0
    minus = 0

    for i in range(3):
        plus += plus_det(A, i)
        minus += minus_det(A, i)

    return plus-minus

def plus_det(A, i):
    b = 1
    for j in range(len(A[0])):
        b *= A[i][j]
        i += 1
    return b

def minus_det(A, i):
    b = 1
    for j in range(len(A[0]) - 1, -1, -1):
        b *= A[i][j]
        i += 1
    return b

line = convertEcuationsToMatrix()[0]
r    = convertEcuationsToMatrix()[1]
det = det(line)
print(det)






# Numpy
# print(np.array(line))
# print(np.array(r))
