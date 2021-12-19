#!/usr/bin/env python3

import os
import sys

# Read lines of input file into an array
lines = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as input:
    lines = input.read().splitlines()

h_pos = 0
depth = 0
aim = 0

commands = {
    'forward': lambda x: globals().update(
        h_pos = h_pos + x,
        depth = depth + (aim * x)
    ),
    'up': lambda x: globals().update(aim = aim - x),
    'down': lambda x: globals().update(aim = aim + x)
}

for command in lines:
    command_array = command.split(' ')
    direction = command_array[0]
    amount = int(command_array[1])
    commands[direction](amount)

print(h_pos * depth)
