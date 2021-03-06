#!/usr/bin/env python

# Temporary until I can update tests to work for solutions using the @timer and @compare decorators.
# The below comment will skip testing this solution when tests are run
# Skip Test

# Import helper functions included in this repository
import time
from helpers import getInput, timer, compare

# Get Data
data = getInput()

# Function to run the For Loop solution using the timer decorator
@timer('For Loop')
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

# Function to run the Zip List Comprehension solution using the timer decorator
@timer('Zip List Comprehension')
def getTimesDepthIncreasedWithZipListComprehension():
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
