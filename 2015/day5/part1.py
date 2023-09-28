#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
santas_list = getInput()


def is_nice(item):
    if any(baddie in item for baddie in ("ab", "cd", "pq", "xy")):
        return False

    item_copy = item
    for vowel in "aeiou":
        item_copy = item_copy.replace(vowel, "")

    if len(item) - len(item_copy) < 3:
        return False

    double_letters = False
    for i in range(len(item) - 1):
        if item[i] == item[i + 1]:
            double_letters = True
            break

    return double_letters


print(len(list(filter(is_nice, santas_list))))
