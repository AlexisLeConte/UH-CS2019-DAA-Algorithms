#!/usr/bin/env python3

INF = 2**64-1

def optimal_chain(i, j, L, T):
    if i == j:
        T[i][j] = 0
    if T[i][j] != INF:
        return T[i][j]
    for k in range(i, j):
        chain_ik = optimal_chain(i, k, L, T)
        chain_kj = optimal_chain(k+1, j, L, T)
        T[i][j] = min(T[i][j], chain_ik + chain_kj + L[i]*L[j+1]*L[k+1])
    return T[i][j]

def optimal_chain_traceback(i, j, L, T):
    if i == j:
        return "{}".format(i)
    for k in range(i, j):
        chain_ik = optimal_chain(i, k, L, T)
        chain_kj = optimal_chain(k+1, j, L, T)
        if T[i][j] == chain_ik + chain_kj + L[i]*L[j+1]*L[k+1]:
            chain_ik = optimal_chain_traceback(i, k, L, T)
            chain_kj = optimal_chain_traceback(k+1, j, L, T)
            return "({}*{})".format(chain_ik, chain_kj)

L = [2,4,8,2,4,8]
T = [[INF for i in range(len(L)-1)] for j in range(len(L)-1)]
print(optimal_chain(0, len(L)-2, L, T))
print(optimal_chain_traceback(0, len(L)-2, L, T))
