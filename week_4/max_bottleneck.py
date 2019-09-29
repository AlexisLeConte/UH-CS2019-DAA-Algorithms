#!/usr/bin/env python3

INF = 2*64-1

def max_bottleneck(source, target, memo):
  if source == target:
    return INF
  if memo[source] != -1:
    return memo[source]
  memo[source] = 0
  for child, capacity in edges[source]:
    memo[source] = max(memo[source], min(capacity, max_bottleneck(child, target, memo)))
  return memo[source]

edges = [[(1,1), (1,3), (2,2)], [(2,4)], [(3,10)], []]
memo = [-1] * len(edges)
print(max_bottleneck(0, 3, memo))
