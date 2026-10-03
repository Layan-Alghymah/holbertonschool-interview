#!/usr/bin/python3
"""Module for determining if all lockboxes can be opened."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, otherwise False."""
    if not boxes:
        return True

    unlocked = {0}
    boxes_to_check = [0]

    while boxes_to_check:
        current_box = boxes_to_check.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                boxes_to_check.append(key)

    return len(unlocked) == len(boxes)
