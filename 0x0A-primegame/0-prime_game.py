#!/usr/bin/python3
"""
0. Prime Game
"""


def isWinner(x, nums):
    """
    prime game to be played by
    Ben & Maria
    Optimal play for both is choosing
    the biggest prime num
    """
    wins = [0, 0]
    sorted_primes = sorted(nums, reverse=True)
    for num in sorted_primes:
        if num == 1:
            wins[1] += 1
            continue
        play = True
        maria = ben = 0
        prime = [True for i in range(num+1)]
        p = 2
        while (p * p) <= num:
            if prime[p]:
                for i in range(p * p, num + 1, p):
                    prime[i] = False
            p += 1
        prime[0] = prime[1] = False
        for value in prime:
            if play and value:
                maria += 1
                play = not play
                continue
            if value and not play:
                ben += 1
                play = not play
                continue
        if play:
            wins[0] += 1
        else:
            wins[1] += 1
        x -= 1
        if x == 0:
            break

    if wins[0] > wins[1]:
        return "Maria"
    elif wins[1] > wins[0]:
        return "Ben"
    else:
        return None
