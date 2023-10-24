#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding.Doc"""


def validUTF8(data):
    """Defines a bitmask to check the most significant bits of the bytes"""
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Initialize a count to track the expected number of trailing bytes
    count = 0

    for byte in data:

        mask_byte = 1 << 7

        if count == 0:

            # Count the number of leading 1s to determine the byte length
            while mask_byte & byte:
                count += 1
                mask_byte = mask_byte >> 1

            # For a single-byte character, count remains 0
            if count == 0:
                continue

            # Invalid encoding if the length is not in [1, 4]
            if count == 1 or count > 4:
                return False

        else:
            # Check if the byte is a valid trailing byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        count -= 1

    if count == 0:
        return True

    return False
