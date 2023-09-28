#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
data = getInput(str)

# Define movement dictionary
move = {
    ">": lambda p: [p[0] + 1, p[1]],
    "<": lambda p: [p[0] - 1, p[1]],
    "^": lambda p: [p[0], p[1] + 1],
    "v": lambda p: [p[0], p[1] - 1],
}

# Initialize variables
houses = 1
santa_position = [0, 0]
robo_position = [0, 0]
positions = [[0, 0]]

# Loop through directions
for index, direction in enumerate(data):
    # Check if index is even
    if index % 2 == 0:
        santa_position = move[direction](santa_position)

        if santa_position not in positions:
            positions.append(santa_position)
            houses += 1
    else:
        robo_position = move[direction](robo_position)

        if robo_position not in positions:
            positions.append(robo_position)
            houses += 1

# Print the solution
print(houses)
