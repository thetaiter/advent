#!/usr/bin/env python

# Import helper functions included in this repository
import argparse
from helpers import getInput, timer, compare

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", help="Specify that this is a test run", action="store_true")
args = parser.parse_args()

# Get Data
data = getInput()

# For Loop Method
@timer('For Loop')
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
@timer('Zip List Comprehension')
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
    return [
        getTimesDepthIncreasedWithForLoop(),
        getTimesDepthIncreasedWithZipListComprehension()
    ]

solution = runSolutions()
if args.test:
    print(solution["return_value"])
