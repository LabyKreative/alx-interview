#!/usr/bin/python3
"""Minimum operations test."""


def minOperations(n):
    """Calculates the fewest number of operations."""
    if not isinstance(n, int):
        return 0
    total_operations = 0
    copy_operations = 0
    characters_done = 1
    # print("H", end='')
    while characters_done < n:
        if copy_operations == 0:
            # init (the first copy all and paste)
            copy_operations = characters_done
            characters_done += copy_operations
            total_operations += 2
            # print("-(11)->{}".format("H" * characters_done), end='')
        elif n - characters_done > 0 and \
                (n - characters_done) % characters_done == 0:
            # copy all and paste
            copy_operations = characters_done
            characters_done += copy_operations
            total_operations += 2
            # print("-(11)->{}".format("H" * characters_done), end='')
        elif copy_operations > 0:
            # paste
            characters_done += copy_operations
            total_operations += 1
            # print("-(01)->{}".format("H" * characters_done), end='')
    # print('')
    return total_operations
