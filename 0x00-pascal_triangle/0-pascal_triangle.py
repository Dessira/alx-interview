#!/usr/bin/python3
"""creates a pascal triangle"""


def pascal_triangle(n):
    """creates a pascal triangle in list format"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    base = [1]
    n = n - 1
    count = 0
    final = [[1]]
    new_base = []
    while count < n:
        new_base.append(1)
        for i in range(len(base) - 1):
            new_base.append(base[i] + base[i + 1])
        new_base.append(1)
        base = new_base
        final.append(new_base)
        count += 1
        new_base = []
    return final
