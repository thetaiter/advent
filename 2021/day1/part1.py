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

# Print the solution
print('For Loop Method:', timesDepthIncreased)
print('Time to calculate:', end - start, 'seconds')

# Zip + List Comprehension Method
start = time.time()
increasedArray = [int(j) > int(i) for i, j in zip(data, data[1:])]
timesDepthIncreased = len([item for item in increasedArray if item == True])
end = time.time()

# Print the solution
print()
print('Zip + List Comprehension Method:', timesDepthIncreased)
print('Time to calculate:', end - start, 'seconds')
