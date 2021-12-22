#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
data = getInput()

# Initialize variables
floor = 0

move = {
    '(': lambda: globals().update(floor = floor + 1),
    ')': lambda: globals().update(floor = floor - 1) if floor >= 0 else True
}

position = 0
for i, char in enumerate(data):
    if move[char]():
        position = i
        break

print(position)
