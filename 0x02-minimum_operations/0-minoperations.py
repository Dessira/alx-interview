#!/usr/bin/python3
"""
 Minimum Operations
"""


def minOperations(n):
    """minimum operations required
    """
    d = n // 2
    while d > 0:
        q, r = divmod(n, d)
        if (r == 0):
            return q + minOperations(d)
        d -= 1
    return 0
