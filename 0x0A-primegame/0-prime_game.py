#!/usr/bin/python3
"""
0. Prime Game
"""


def isWinner(x, nums):
    """
    prime game to be played by
    Ben & Maria
    """
    ben = 0
    maria = 0
    play = True
    j = 0
    winner = [0, 0]
    while x > 0:
        ben = 0
        maria = 0
        num = nums[j]
        if num == 1:
            winner[1] += 1
        else:
            p = 2
            prime = [True for i in range(num+1)]
            while (p * p) <= num:
                if prime[p] == True:
                    for i in range(p * p, num + 1, p):
                        prime[i] = False
            for idx in range(len(prime)):
                if play:
                    if prime[idx]:
                        maria += 1
                else:
                    if prime[idx]:
                        ben += 1
                play = not play

            if maria > ben:
                winner[0] += 1
            if ben > maria:
                winner[1] += 1
        x -= 1
        j += 1
    if winner[0] > winner[1]:
        return "Maria"
    elif winner[1] > winner[0]:
        return "Ben"
    else:
        return None
