#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_prime(nums):
        for num in nums:
            if is_prime(num):
                return num
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_player = "Maria"

        while True:
            prime = get_next_prime(nums)
            if prime is None:
                break

            nums = [num for num in nums if num % prime != 0]

            if current_player == "Maria":
                current_player = "Ben"
            else:
                current_player = "Maria"

        if current_player == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
