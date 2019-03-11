import re
import numpy as np
import copy

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
def simpleDet(A):
    d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return  d
def det(A):
    copyA = copy.deepcopy(A)
    copyA.append(copyA[0])
    copyA.append(copyA[1])
    plus  = 0
    minus = 0

    for i in range(3):
        plus += plus_det(copyA, i)
        minus += minus_det(copyA, i)

    return plus-minus

def plus_det(copyA, i):
    b = 1
    for j in range(len(copyA[0])):
        b *= copyA[i][j]
        i += 1
    return b

def minus_det(copyA, i):
    b = 1
    for j in range(len(copyA[0]) - 1, -1, -1):
        b *= copyA[i][j]
        i += 1
    return b

def trans(A):
    copyA = copy.deepcopy(A)
    for i in range(len(copyA)):
        for j in range(len(copyA)):
            copyA[i][j] = A[j][i]
    return copyA

def truncateMatrix(matrix, i, j):
    cc = copy.deepcopy(matrix)
    cc.remove(cc[i])
    l = len(cc[0])
    for k in range(l-1):
        del cc[k][j]
    return cc

def matrixStar(A):
    copyA = copy.deepcopy(A)
    for i in range(len(copyA)):
        for j in range(len(copyA)):
            d = simpleDet(truncateMatrix(A,i,j))
            copyA[i][j] = ((-1) ** (i+j)) * d
    return copyA

def inverse(A, star, det):
    copyA = copy.deepcopy(A)
    for i in range(len(star)):
        for j in range(len(star)):
            copyA[i][j] = star[i][j] / det
    return copyA

line  = convertEcuationsToMatrix()[0]
r     = convertEcuationsToMatrix()[1]
det   = det(line)
trans = trans(line)
star  = matrixStar(line)
inv   = inverse(line, star, det)










# Numpy
# print(np.array(line))
# print(np.array(r))
