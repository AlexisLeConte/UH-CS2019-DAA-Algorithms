#!/usr/bin/env python3

def dfs_order(n, E, C, T):
    # explore all children
    for c in E[n]:
        if C[c] == 0:
            dfs_order(c, E, C, T)

    # mark this node as computed
    C[n] = 1
    T.append(n)

def topological_order(V, E):
    # reversed topological order
    T = []

    # keep track of computed nodes
    C = [0] * len(V)

    # dfs topological order
    for n in range(len(V)):
        if C[n] == 0:
            dfs_order(n, E, C, T)

    # return the topological order
    return list(reversed(T))

V = [n for n in range(5)]
E = [[1, 2], [3], [3, 4], [4], []]
print(topological_order(V, E))
