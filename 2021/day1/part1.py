#!/usr/bin/env python3

import os
import sys
import time

# Read lines of input file into an array
lines = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as input:
   lines = input.read().splitlines()

timesDepthIncreased = 0

# For Loop Method
start = time.time()

for i, line in enumerate(lines):
    if i > 0:
        previousDepth = int(lines[i-1])
        currentDepth = int(line)

        if currentDepth > previousDepth:
            timesDepthIncreased += 1

end = time.time()

print('For Loop Method:', timesDepthIncreased)
print('Time to calculate:', end - start, 'seconds')

# Zip + List Comprehension Method
start = time.time()
increasedArray = [int(j) > int(i) for i, j in zip(lines, lines[1:])]
timesDepthIncreased = len([item for item in increasedArray if item == True])
end = time.time()

print()
print('Zip + List Comprehension Method:', timesDepthIncreased)
print('Time to calculate:', end - start, 'seconds')