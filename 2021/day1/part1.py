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
    if i > 0:
        previousDepth = int(lines[i-1])
        currentDepth = int(line)

        if currentDepth > previousDepth:
            timesDepthIncreased += 1

print(timesDepthIncreased)

# Zip + List Comprehension Method
increasedArray = [int(j) > int(i) for i, j in zip(lines, lines[1:])]
timesDepthIncreased = len([item for item in increasedArray if item == True])

print(timesDepthIncreased)
