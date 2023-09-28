#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
data = getInput()
data = [box.split("x") for box in data]

# Calculate feet of ribbon
feet_of_ribbon = 0
for box in data:
    bow = eval("*".join(box))
    box = [int(side) for side in box]
    box.remove(max(box))
    wrap = 2 * sum(box)
    feet_of_ribbon += wrap + bow

# Print the solution
print(feet_of_ribbon)
