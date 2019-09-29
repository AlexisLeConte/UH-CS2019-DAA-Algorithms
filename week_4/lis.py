#!/usr/bin/env python3

def LIS(A):
  L = [0] * len(A)
  L[0] = 1
  for i in range(1, len(A)):
    for j in range(i):
      if A[j] < A[i]:
        L[i] = max(L[i], L[j] + 1)
  length, index = L[0], 0
  for i in range(1, len(L)):
    if length < L[i]:
      length, index = L[i], i
  return length, index, L

def LIS_traceback(A, L, index):
  T = []
  T.append(A[index])
  for i in reversed(range(index)):
    if A[i] < A[index] and L[i] == L[index]-1:
      T.append(A[i])
      index = i
  return T

A = [1, 5, 2, 7, 4, 3, 6, 8, 9]
length, index, L = LIS(A)
T = LIS_traceback(A, L, index)
print(L)
while len(T) > 0:
  print(T.pop())
