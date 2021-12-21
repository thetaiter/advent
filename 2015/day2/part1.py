#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
data = getInput()
data = [[int(side) for side in box.split('x')] for box in data]

# Calculate surface area
total_surface_area = 0
for box in data:
    sides = [x * y for x, y in zip(box, [box[1], box[2], box[0]])]
    surface_area = 2 * sum(sides)
    extra = min(sides)
    total_surface_area += surface_area + extra

# Print the solution
print(total_surface_area)
