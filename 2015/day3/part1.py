#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
data = getInput()

# Define movement dictionary
move = {
    ">": lambda p: [p[0] + 1, p[1]],
    "<": lambda p: [p[0] - 1, p[1]],
    "^": lambda p: [p[0], p[1] + 1],
    "v": lambda p: [p[0], p[1] - 1],
}

# Initialize variables
houses = 1
position = [0, 0]
positions = [[0, 0]]

# Loop through directions
for direction in data:
    position = move[direction](position)

    if position not in positions:
        positions.append(position)
        houses += 1

# Print the solution
print(houses)
