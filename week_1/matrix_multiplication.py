#!/usr/bin/env python3

def matrix_multiplication(a, b):
  """Returns the result of the matrix multiplication of a and b.
  a and b are square matrices of the same size"""

  c = [[0 for i in range(len(a))] for j in range(len(a))]
  for i in range(len(a)):
    for j in range(len(a)):
      for k in range(len(a)):
        c[i][j] += a[i][k] * b[k][j]
  return c
