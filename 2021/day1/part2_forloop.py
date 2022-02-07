#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput, timer

# Get Data
data = getInput()

# For Loop Method
@timer
def getTimesDepthIncreased():
    timesDepthIncreased = 0

    for i, line in enumerate(data):
        if i > 0 and i < len(data)-2:
            previousDepth = int(data[i-1]) + int(data[i]) + int(data[i+1])
            currentDepth = int(data[i]) + int(data[i+1]) + int(data[i+2])

            if currentDepth > previousDepth:
                timesDepthIncreased += 1

    print(timesDepthIncreased)

# Run the solution for the For Loop Method
getTimesDepthIncreased()
