#!/usr/bin/env python3

import os
import sys

# Read lines of input file into an array
lines = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as input:
   lines = input.read().splitlines()

# For Loop Method
timesDepthIncreased = 0
for i, line in enumerate(lines):
    if i > 0 and i < len(lines)-2:
        previousDepth = int(lines[i-1]) + int(lines[i]) + int(lines[i+1])
        currentDepth = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])

        if currentDepth > previousDepth:
            timesDepthIncreased += 1

print(timesDepthIncreased)

# Zip + List Comprehension Method
depthArray = [int(j) + int(i) + int(k) for i, j, k in zip(lines, lines[1:], lines[2:])]
increasedArray = [int(j) > int(i) for i, j in zip(depthArray, depthArray[1:])]
timesDepthIncreased = len([item for item in increasedArray if item == True])

print(timesDepthIncreased)
