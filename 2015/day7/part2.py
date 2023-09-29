#!/usr/bin/env python

# Import helper functions included in this repository
from common import get_wire_signals
from helpers import getInput

# Get Data
instructions = getInput()

# Solution
wire_a = get_wire_signals(instructions)["a"]

for index in range(len((instructions))):
    if instructions[index].endswith(" -> b"):
        instructions[index] = f"{wire_a} -> b"

print(get_wire_signals(instructions)["a"])
