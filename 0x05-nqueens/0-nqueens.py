#!/usr/bin/python3
"""
N non-attacking queens on an N×N chessboard
Print every solution to the problem, one-per-line
"""

import sys


def n_queens(n, row, result):
    if row == n:
        print(result)
    else:
        for col in range(n):
            if all(c != col and
                   r + c != row + col and
                   r - c != row - col for r, c in result):
                result.append([row, col])
                n_queens(n, row + 1, result)
                result.remove([row, col])
