#!/usr/bin/python3
"""Checks if if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """checks if data represents a valid encoding
    """
    holder = []
    for val in data:
        holder.append(val)
    try:
        bytes(holder).decode()
    except (ValueError, UnicodeError):
        return False
    else:
        return True
