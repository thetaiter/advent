#!/usr/bin/env python

# For timing the different methods
import time

# Import helper functions included in this repository
from helpers import getInput

# Get Data
data = getInput()

# Initialize variables
timesDepthIncreased = 0

# For Loop Method
start = time.time()
for i, depth in enumerate(data):
    if i > 0:
        previousDepth = int(data[i-1])
        currentDepth = int(depth)

        if currentDepth > previousDepth:
            timesDepthIncreased += 1
end = time.time()

# Print the solution for the For Loop Method
print(timesDepthIncreased)
print('Time to calculate:', end - start, 'seconds')
