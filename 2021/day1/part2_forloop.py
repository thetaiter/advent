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
for i, line in enumerate(data):
    if i > 0 and i < len(data)-2:
        previousDepth = int(data[i-1]) + int(data[i]) + int(data[i+1])
        currentDepth = int(data[i]) + int(data[i+1]) + int(data[i+2])

        if currentDepth > previousDepth:
            timesDepthIncreased += 1
end = time.time()

# Print the solution for the For Loop Method
print(timesDepthIncreased)
print('Time to calculate:', end - start, 'seconds')
