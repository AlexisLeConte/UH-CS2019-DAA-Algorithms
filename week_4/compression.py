#!/usr/bin/env python3

import zlib
from random import randint

def zlib_cost(A, i, j):
  return len(zlib.compress(A[i:j+1]))

def dummy_cost(A, i, j):
  cost = 1
  for k in range(i, j):
    if A[k] != A[k+1]:
      cost += 1
  return cost

def optimal_partitioning(A, cost):
  M = [0] * len(A)
  M[0] = cost(A, 0, 0)
  for i in range(1, len(A)):
    M[i] = cost(A, 0, i)
    for j in range(i):
      M[i] = min(M[i], M[j] + cost(A, j+1, i))
  return M[len(A)-1]

data = b'some data to be compressed...'
print(len(data), data)
print(optimal_partitioning(data, zlib_cost))
print(optimal_partitioning(data, dummy_cost))

data = b'AAAABBAAAAABBBBAACCCCCAAABCACCCCC'
print(len(data), data)
print(optimal_partitioning(data, zlib_cost))
print(optimal_partitioning(data, dummy_cost))

data = bytearray([randint(0, 10) for i in range(100)])
print(len(data), data)
print(optimal_partitioning(data, zlib_cost))
print(optimal_partitioning(data, dummy_cost))
