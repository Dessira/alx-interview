#!/usr/bin/python3
"""Defines Lockboxes function"""

def canUnlockAll(boxes):
    """Function checks if all boxes can be opened based on the keys present in the boxes
    """
    # holder for keys
    holder = dict()
    count = 0
    if len(boxes) == 0:
        return False

    for box in boxes:
        if len(box) > 1:
            for i in range(len(box) - 1):
                if box[i] not in holder and box[i] != i:
                    holder[box[i]] = count
                elif box[i] in holder and box[i] == i:
                    holder[box[i]] = count
        else:
            if len(box) == 1 and box[0] != count:
                val = box[0]
                holder[val] = count
        count += 1
    for j in range(len(boxes) - 1):
        if j > 0 and j not in holder:
            return False
    return True
