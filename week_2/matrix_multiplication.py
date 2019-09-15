#!/usr/bin/env python3

number_of_additions = 0
number_of_multiplications = 0

def split(m):
    """Split a matrix into 4 quadrants."""

    m11 = [m[i][:len(m)//2] for i in range(0, len(m)//2)]
    m12 = [m[i][len(m)//2:] for i in range(0, len(m)//2)]
    m21 = [m[i][:len(m)//2] for i in range(len(m)//2, len(m))]
    m22 = [m[i][len(m)//2:] for i in range(len(m)//2, len(m))]
    return m11, m12, m21, m22

def merge(m11, m12, m21, m22):
    """Merge back 4 matrix quadrants into a single matrix."""

    m = []
    for i in range(len(m11)):
        m.append(m11[i] + m12[i])
    for i in range(len(m21)):
        m.append(m21[i] + m22[i])
    return m

def matrix_addition(a, b):
    """Add 2 matrices a and b of the same size."""

    global number_of_additions
    number_of_additions += len(a) * len(a[0])
    return [[a[j][i] + b[j][i] for i in range(len(a))] for j in range(len(a))]

def matrix_multiplication(a, b):
    """Multiply 2 square matrices a and b of the same size.
    The size of the matrices must be a power of 2."""

    if len(a) == 1:
        global number_of_multiplications
        number_of_multiplications += 1
        return [[a[0][0] * b[0][0]]]
    a11, a12, a21, a22 = split(a)
    b11, b12, b21, b22 = split(b)
    c11 = matrix_addition(matrix_multiplication(a11, b11), matrix_multiplication(a12, b21))
    c12 = matrix_addition(matrix_multiplication(a11, b12), matrix_multiplication(a12, b22))
    c21 = matrix_addition(matrix_multiplication(a21, b11), matrix_multiplication(a22, b21))
    c22 = matrix_addition(matrix_multiplication(a21, b12), matrix_multiplication(a22, b22))
    return merge(c11, c12, c21, c22)
