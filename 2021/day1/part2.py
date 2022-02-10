#!/usr/bin/env python

# Temporary until I can update tests to work for solutions using the @timer and @compare decorators.
# The below comment will skip testing this solution when tests are run
# Skip Test

# Import helper functions included in this repository
from helpers import getInput, timer, compare

# Get Data
data = getInput()

# For Loop Method
@timer
def getTimesDepthIncreasedWithForLoop():
    timesDepthIncreased = 0

    for i, line in enumerate(data):
        if i > 0 and i < len(data)-2:
            previousDepth = int(data[i-1]) + int(data[i]) + int(data[i+1])
            currentDepth = int(data[i]) + int(data[i+1]) + int(data[i+2])

            if currentDepth > previousDepth:
                timesDepthIncreased += 1

    print(timesDepthIncreased)
    return timesDepthIncreased

# Zip + List Comprehension Method
@timer
def getTimesDepthIncreasedWithZipListComprehension():
    timesDepthIncreased = 0

    depthArray = [int(j) + int(i) + int(k) for i, j, k in zip(data, data[1:], data[2:])]
    increasedArray = [int(j) > int(i) for i, j in zip(depthArray, depthArray[1:])]
    timesDepthIncreased = len([item for item in increasedArray if item == True])

    print(timesDepthIncreased)
    return timesDepthIncreased

# Run the solutions and compare them
@compare
def runSolutions():
    getTimesDepthIncreasedWithForLoop()
    getTimesDepthIncreasedWithZipListComprehension()

runSolutions()
