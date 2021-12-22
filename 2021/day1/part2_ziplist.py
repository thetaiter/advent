#!/usr/bin/env python

# For timing the different methods
import time

# Import helper functions included in this repository
from helpers import getInput

# Get Data
data = getInput()

# Initialize variables
timesDepthIncreased = 0

# Zip + List Comprehension Method
start = time.time()
depthArray = [int(j) + int(i) + int(k) for i, j, k in zip(data, data[1:], data[2:])]
increasedArray = [int(j) > int(i) for i, j in zip(depthArray, depthArray[1:])]
timesDepthIncreased = len([item for item in increasedArray if item == True])
end = time.time()

# Print the solution for the Zip + List Comprehension Method
print(timesDepthIncreased)
print('Time to calculate:', end - start, 'seconds')
