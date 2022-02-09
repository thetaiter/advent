#!/usr/bin/env python

# Import helper functions included in this repository
import time
from helpers import getInput, timer, compare

# Get Data
data = getInput()

@timer('For Loop Method')
def getTimesDepthIncreasedWithForLoop():
    timesDepthIncreased = 0

    for i, depth in enumerate(data):
        if i > 0:
            previousDepth = int(data[i-1])
            currentDepth = int(depth)

            if currentDepth > previousDepth:
                timesDepthIncreased += 1

    print(f"{timesDepthIncreased}")
    return timesDepthIncreased

@timer('Zip List Comprehension Method')
def getTimesDepthIncreasedWithZipListComprehension():
    timesDepthIncreased = 0

    increasedArray = [int(j) > int(i) for i, j in zip(data, data[1:])]
    timesDepthIncreased = len([item for item in increasedArray if item == True])

    print(f"{timesDepthIncreased}")
    return timesDepthIncreased

# Run the solutions and compare them
@compare
def runSolutions():
    return [
        getTimesDepthIncreasedWithForLoop(),
        getTimesDepthIncreasedWithZipListComprehension()
    ]

runSolutions()
