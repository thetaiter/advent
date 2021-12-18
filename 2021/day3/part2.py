#!/usr/bin/env python3

import os
import sys

# Read lines of input file into an array
lines = []
with open(os.path.join(sys.path[0], './input.txt'), 'r') as input:
   lines = input.read().splitlines()

# Initialize arrays with length of the first line in the input file
length = len(lines[0])
gamma_rate = [0] * length
ones = [0] * length
zeros = [0] * length

for line in lines:
    for i, char in enumerate(line):
        if char == "0":
            zeros[i] += 1
        else:
            ones[i] += 1

for i, number in enumerate(zeros):
    if zeros[i] > ones[i]:
        gamma_rate[i] = 0
    else:
        gamma_rate[i] = 1

def arrayToString(array):
    return ''.join(map(str,array))

def binaryArrayToDecimal(binaryArray):
    return int(arrayToString(binaryArray), 2)

def invertBinaryArray(binaryArray):
    return [1 if i == 0 else 0 for i in binaryArray]

epsilon_rate = binaryArrayToDecimal(invertBinaryArray(gamma_rate))
gamma_rate = binaryArrayToDecimal(gamma_rate)

print('Gamme Rate:', gamma_rate)
print('Epsilon Rate:', epsilon_rate)
print('Power Consumption:', gamma_rate*epsilon_rate)
