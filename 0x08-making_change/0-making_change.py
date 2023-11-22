#!/usr/bin/python3
"""
A function that determine the fewest number of coins
needed to meet a given amount total.
"""


def makeChange(coins, total):
    # Initialize a list 'dp' to store the minimum number of
    # coins needed for each total amount.
    # Set the initial value to infinity for all amounts except 0.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin to update the 'dp' array.
    for coin in coins:
        # For each coin, iterate through the 'dp' array from the
        # coin value to the total amount.
        for i in range(coin, total + 1):
            # Update the 'dp' value by taking the minimum
            # of the current value and the value
            # obtained by subtracting the coin value from the
            # current amount, plus 1.
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the final 'dp' value for the total amount is still infinity,
    # it means it's not possible to make change for that amount.
    if dp[total] == float('inf'):
        return -1

    # Return the minimum number of coins needed for the given total amount.
    return dp[total]
