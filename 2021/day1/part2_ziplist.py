#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput, timer

# Get Data
data = getInput()

# Zip + List Comprehension Method
@timer
def getTimesDepthIncreased():
    timesDepthIncreased = 0

    depthArray = [int(j) + int(i) + int(k) for i, j, k in zip(data, data[1:], data[2:])]
    increasedArray = [int(j) > int(i) for i, j in zip(depthArray, depthArray[1:])]
    timesDepthIncreased = len([item for item in increasedArray if item == True])

    print(timesDepthIncreased)

# Run the solution for the Zip + List Comprehension Method
getTimesDepthIncreased()
