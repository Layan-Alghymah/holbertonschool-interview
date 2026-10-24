#!/usr/bin/python3
"""Validate UTF-8 encoded data."""


def validUTF8(data):
    """Return True if data is valid UTF-8, otherwise False."""
    data = [number & 0xFF for number in data]
    i = 0

    while i < len(data):
        first = data[i]

        if first <= 0x7F:
            length = 1
        elif 0xC2 <= first <= 0xDF:
            length = 2
        elif 0xE0 <= first <= 0xEF:
            length = 3
        elif 0xF0 <= first <= 0xF4:
            length = 4
        else:
            return False

        if i + length > len(data):
            return False

        for j in range(1, length):
            byte = data[i + j]

            if byte & 0xC0 != 0x80:
                return False

            if j == 1:
                if first == 0xE0 and byte < 0xA0:
                    return False
                if first == 0xED and byte > 0x9F:
                    return False
                if first == 0xF0 and byte < 0x90:
                    return False
                if first == 0xF4 and byte > 0x8F:
                    return False

        i += length

    return True
