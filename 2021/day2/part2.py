#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
data = getInput()

# Initialize variables
h_pos = 0
depth = 0
aim = 0

# Define commands dictionary using lambda functions
commands = {
    'forward': lambda x: globals().update(
        h_pos = h_pos + x,
        depth = depth + (aim * x)
    ),
    'up': lambda x: globals().update(aim = aim - x),
    'down': lambda x: globals().update(aim = aim + x)
}

# Iterate through and execute commands
for command in data:
    command_array = command.split(' ')
    direction = command_array[0]
    amount = int(command_array[1])
    commands[direction](amount)

# Print the solution
print(h_pos * depth)
