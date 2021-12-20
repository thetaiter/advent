#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
data = getInput()

# Initialize variables
floor = 0

move = {
    '(': lambda: globals().update(floor = floor + 1),
    ')': lambda: globals().update(floor = floor - 1),   
}

for char in data:
    move[char]()

print(floor)
