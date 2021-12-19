#!/usr/bin/env python3

import os
import sys

# Read lines of input file into an array
lines = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as input:
    lines = input.read().splitlines()

# Initialize variables
h_pos = 0
depth = 0

# Define commands dictionary using lambda functions
commands = {
    'forward': lambda x: globals().update(h_pos = h_pos + x),
    'up': lambda x: globals().update(depth = depth - x),
    'down': lambda x: globals().update(depth = depth + x)
}

# Iterate through and execute commands
for command in lines:
    command_array = command.split(' ')
    direction = command_array[0]
    amount = int(command_array[1])
    commands[direction](amount)

# Print the solution
print(h_pos * depth)
