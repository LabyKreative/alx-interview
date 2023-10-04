#!/usr/bin/python3
"""Lockboxes module.
"""


def canUnlockAll(boxes):
    """Verify if unlocking the first box allows access to all other
    bosex in a list by using the keys (indices) within the boxes.
    """
    n = len(boxes)
    unlocked_boxes = set([0])
    locked_boxes = set(boxes[0]).difference(set([0]))
    while len(locked_boxes) > 0:
        box_key = locked_boxes.pop()
        if not box_key or box_key >= n or box_key < 0:
            continue
        if box_key not in unlocked_boxes:
            locked_boxes = locked_boxes.union(boxes[box_key])
            unlocked_boxes.add(box_key)
    return n == len(unlocked_boxes)
