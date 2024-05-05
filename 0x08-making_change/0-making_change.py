#!/usr/bin/python3
"""
Module 1: Minimum Coins to make change
"""


def makeChange(coins, total):
    """
    return minimum amount of coins
    """
    sorted_coins = sorted(coins)
    if total <= 0 or not isinstance(total, int):
        return 0
    num = 0
    n = len(coins) - 1
    while n >= 0:
        while total >= sorted_coins[n]:
            total -= sorted_coins[n]
            num += 1
            if total == 0:
                return num
        n -= 1
    if total > 0:
        return -1