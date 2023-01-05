#!/usr/bin/python3
"""Defines Lockboxes function"""

def canUnlockAll(boxes):
    """Function checks if all boxes can be opened based on the keys present in the boxes
    """
    # holder for keys
    holder = dict()
    count = 0

    for box in boxes:
        if len(box) > 1:
            for i in range(len(box) - 1):
                if box[i] not in holder:
                    holder[i] = count
        else:
            if len(box) == 1:
                val = box[0]
                holder[val] = count
        count += 1

    for i in range(len(boxes) - 1):
        if i in holder:
            if holder[i] == holder.get(holder[i]):
                return False
    return True
