#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returns perimeter of an island"""
    perimeter = 0
    if type(grid) != list:
        return 0
    g = len(grid)
    for x, row in enumerate(grid):
        r = len(row)
        for y, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                x == 0 or (len(grid[x - 1]) > y and grid[x - 1][y] == 0),
                y == r - 1 or (r > y + 1 and row[y + 1] == 0),
                x == g - 1 or (len(grid[x + 1]) > y and grid[x + 1][y] == 0),
                y == 0 or row[y - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
