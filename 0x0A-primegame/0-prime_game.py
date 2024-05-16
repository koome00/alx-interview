#!/usr/bin/python3
"""
0. Prime Game
"""


def isWinner(x, nums):
    """
    prime game to be played by
    Ben & Maria
    """
    wins = [0, 0]
    maria = ben = 0
    num = max(nums)
    play = True
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p) <= num:
        if prime[p] == True:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    prime[0] = prime[1] = False
    for value in prime:
        if play and value:
            maria += 1
        if value and not play:
            ben += 1
        play = not play
    if maria > ben:
        wins[0] += 1
    if maria < ben:
        wins[1] += 1
    if wins[0] > wins[1]:
        return "Maria"
    elif wins[1] > wins[0]:
        return "Ben"
    else:
        return None
