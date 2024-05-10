#!/usr/bin/python3
"""
Module 1: Island Perimeter
"""


def island_perimeter(grid):
    """
    returns perimeter of a wall
    """
    total_peri = 0
    assert (len(grid) <= 100)
    for x, row in enumerate(grid):
        assert (len(row) <= 100)
        for y, element in enumerate(row):
            if element == 1:
                peri = 4
                # check bottom upto second last row
                if x < (len(grid) - 1):
                    if grid[x+1][y] == 1:
                        peri = peri - 1
                # check right upto second last column
                if y < (len(row) - 1):
                    if grid[x][y+1] == 1:
                        peri = peri - 1
                # check top upto second last row
                if x > 0:
                    if grid[x-1][y] == 1:
                        peri = peri - 1
                # check left upto second last column
                if y > 0:
                    if grid[x][y-1] == 1:
                        peri = peri - 1
                total_peri = peri + total_peri
    return total_peri
