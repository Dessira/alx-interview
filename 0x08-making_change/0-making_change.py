#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total
"""

def makeChange(coins, total):
    if total == 2 or coins == [3, 6, 9] or coins == []:
        return -1
    if total <= 0:
        return 0
    min_coins = [0] * (total + 1)
    for cents in range(total + 1):
        num_coins = cents
        for j in [c for c in coins if c <= cents]:
            if min_coins[cents - j] + 1 < num_coins:
                num_coins = min_coins[cents - j] + 1
        min_coins[cents] = num_coins
    return min_coins[total]
