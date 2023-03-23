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


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except IndexError:
        print("Usage: nqueens N") or exit(1)
    except ValueError:
        print("N must be a number") or exit(1)
    else:
        if n < 4:
            print("N must be at least 4") or exit(1)
        else:
            n_queens(n, 0, [])
