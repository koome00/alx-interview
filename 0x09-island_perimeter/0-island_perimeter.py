#!/usr/bin/python3
"""
Module 1: Island Perimeter
"""


def island_perimeter(grid):
    """
    returns perimeter of a wall
    """
    total_peri = 0
    for x, row in enumerate(grid):
        for y, element in enumerate(row):
            if element == 1:
                peri = 4
                # check bottom upto second last row
                if grid[x+1][y] == 1 and x < (len(grid)-1):
                    peri = peri - 1
                # check right upto second last column
                if grid[x][y+1] == 1 and y < (len(grid)-1):
                    peri = peri - 1
                # check top upto second last row
                if grid[x-1][y] == 1 and x > 0:
                    peri = peri - 1
                # check left upto second last column
                if grid[x][y-1] == 1 and y > 0:
                    peri = peri - 1
                if peri == 4:
                    peri = 0
                total_peri = peri + total_peri
    return total_peri
