#!/usr/bin/env python3

from math import log2, floor
from random import shuffle

def random_permutation(n):
  array = [i for i in range(n)]
  shuffle(array)
  return array

def index_of_min(A, i, j):
    m = min(A[i:i+pow(2,j)])
    for i in range(len(A)):
        if A[i] == m:
            return i
    return -1

def algorithm(A):
    M = [[0 for j in range(1+int(log2(len(A))))] for i in range(len(A))]
    for i in range(len(A)):
        M[i][0] = i
    for j in range(1, 1+int(log2(len(A)))):
        for i in range(len(A)+1-pow(2,j)):
            if A[M[i][j-1]] <= A[M[i+pow(2,j-1)][j-1]]:
                M[i][j] = M[i][j-1]
            else:
                M[i][j] = M[i+pow(2,j-1)][j-1]
            assert index_of_min(A, i, j) == M[i][j], "Guess does not hold"
    return M

def query(A, l, r):
    M = algorithm(A)
    k = floor(log2(r-l+1))
    return min(A[M[l][k]], A[M[r-pow(2,k)+1][k]])

A = random_permutation(2**3)
print(A, query(A, 0, 3))
