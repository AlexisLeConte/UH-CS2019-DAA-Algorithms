#!/usr/bin/env python3

def merge(a, b):
    """Merge 2 sorted arrays a and b into a single sorted array."""

    res = []
    index_a, index_b = 0, 0
    while index_a != len(a) and index_b != len(b):
        if a[index_a] < b[index_b]:
            res.append(a[index_a])
            index_a += 1
        else:
            res.append(b[index_b])
            index_b += 1
    for i in range(index_a, len(a)):
        res.append(a[i])
    for i in range(index_b, len(b)):
        res.append(b[i])
    return res

def kway_merge(arrays):
    """Merge a list of sorted arrays into a single sorted array."""

    if len(arrays) == 0:
        return []
    if len(arrays) == 1:
        return arrays[0]
    if len(arrays) == 2:
        return merge(arrays[0], arrays[1])

    merged_l = kway_merge(arrays[:len(arrays) // 2])
    merged_r = kway_merge(arrays[len(arrays) // 2:])
    return merge(merged_l, merged_r)
