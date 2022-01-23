import random
import numpy as np

n = 5

A = [[random.Random(1, 100) for i in range(n)] for j in range(n)]

M = [[96, 68, 96, 26, 87], [98, 90, 3, 73, 94], [32, 27, 39, 78, 20], [8, 38, 95, 30, 30], [92, 13, 12, 65, 1]]


''' def desno(matrica):
    n = len(matrica[0])
    for j in range(n // 2):
        for i in range(j, n - j - 1):
            temp = matrica[j][i]
            matrica[j][i] = matrica[n - 1 - i][j]
            matrica[n - 1 - i][j] = matrica[n - 1 - j][n - 1 - i]
            matrica[n - 1 - j][n - 1 - i] = matrica[i][n - 1 - j]
            matrica[i][n - 1 - j] = temp
    return matrica 


print(np.matrix(M))
print(np.matrix(desno(M))) '''


def desno(matrica):

    n = len(matrica[0])

    B = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            B[i][j] = matrica[n - j - 1][i]
    return B

def levo(matrica):

    n = len(matrica[0])

    C = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = matrica[j][n - i - 1]
    return C

def flip_H(matrica):

    n = len(matrica[0])

    C = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = matrica[n - i - 1][j]
    return C


def flip_V(matrica):

    n = len(matrica[0])

    C = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = matrica[i][n - j - 1]
    return C


def flip_GD(matrica):

    n = len(matrica[0])

    C = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = matrica[j][i]
    return C

def flip_SD(matrica):
    C = levo(matrica)
    C = flip_GD(C)
    C = desno(C)
    return C


print(np.matrix(M))
print(np.matrix(flip_SD(M)))
