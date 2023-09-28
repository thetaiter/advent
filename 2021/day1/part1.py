#!/usr/bin/env python

# Import helper functions included in this repository
import argparse
from helpers import getInput, timer, compare

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "-t", "--test", help="Specify that this is a test run", action="store_true"
)
args = parser.parse_args()

# Get Data
data = getInput()


# Function to run the For Loop solution using the timer decorator
@timer("For Loop")
def getTimesDepthIncreasedWithForLoop():
    timesDepthIncreased = 0

    for i, depth in enumerate(data):
        if i > 0:
            previousDepth = int(data[i - 1])
            currentDepth = int(depth)

            if currentDepth > previousDepth:
                timesDepthIncreased += 1

    print(f"{timesDepthIncreased}")
    return timesDepthIncreased


# Function to run the Zip List Comprehension solution using the timer decorator
@timer("Zip List Comprehension")
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
        getTimesDepthIncreasedWithZipListComprehension(),
    ]


solution = runSolutions()
if args.test:
    print(solution["return_value"])
