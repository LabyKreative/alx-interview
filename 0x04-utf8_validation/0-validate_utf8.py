#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding.Doc"""


def validUTF8(data):
    # Define a bitmask to check the most significant bits of the bytes
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Initialize a count to track the expected number of trailing bytes
    count = 0

    for byte in data:
        if count == 0:
            if byte & mask1 == 0:
                continue
            # Count the number of leading 1s to determine the byte length
            while byte & mask1:
                count += 1
                byte <<= 1
            # Invalid encoding if the length is not in [1, 4]
            if count == 1 or count > 4:
                return False
            # For a single-byte character, count remains 0
            if count == 0:
                continue
        else:
            # Check if the byte is a valid trailing byte
            if not (byte & mask1 and not byte & mask2):
                return False
            count -= 1

    # All bytes have been checked, and the count should be 0 if it's valid UTF-8
    return count == 0
