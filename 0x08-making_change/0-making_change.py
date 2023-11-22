#!/usr/bin/python3
"""
A function that determine the fewest number of coins
needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Calculate the min num of coins needed to make change for a given amount.

    Args:
        coins (list): List of coin denominations available.
        total (int): The total amount for which change needs to be made.

    Returns:
        int: Min num of coins needed. Returns -1 if change cannot be made.
    """
    if total <= 0:
        return 0

    remaining_amount = total
    coins_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while remaining_amount > 0:
        if coin_index >= num_coins:
            return -1

        if remaining_amount - sorted_coins[coin_index] >= 0:
            remaining_amount -= sorted_coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1

    return coins_count
