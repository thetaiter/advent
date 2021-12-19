#!/usr/bin/env python3

import os
import sys

# Read lines of input file into an array
lines = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as input:
    lines = input.read().splitlines()

horizontal_position = 0
depth = 0

commands = {
    'forward': lambda x: globals().update(horizontal_position=horizontal_position+x),
    'up': lambda x: globals().update(depth=depth-x),
    'down': lambda x: globals().update(depth=depth+x)
}

for command in lines:
    command_array = command.split(' ')
    direction = command_array[0]
    amount = int(command_array[1])
    commands[direction](amount)

print(horizontal_position*depth)
