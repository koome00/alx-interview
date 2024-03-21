#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters
in the file
"""


def minOperations(n):
    """
    adds the prime multiple of a n to find minimum number of
    operations to result to H character printed n times
    """
    div = 2
    num_operations = 0
    if n == 1:
        return num_operations
    while n > 1:
        while n % div:
            div += 1
        num_operations += div
        n = n // div
    return num_operations
