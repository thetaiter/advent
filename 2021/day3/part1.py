#!/usr/bin/env python3

import os
import sys

# Read lines of input file into an array
lines = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as input:
   lines = input.read().splitlines()

# Initialize arrays with length of the first line in the input file
length = len(lines[0])
ones = [0] * length
zeros = [0] * length
gamma_rate_binary = ''

# Calculate number of ones and zeroes for each bit
for line in lines:
    for i, char in enumerate(line):
        if char == '0':
            zeros[i] += 1
        else:
            ones[i] += 1

# Determine gamma rate binary from the number of ones and zeroes in each bit
for i in range(length):
    if zeros[i] > ones[i]:
        gamma_rate_binary += '0'
    else:
        gamma_rate_binary += '1'

# Invert every bit in a binary string
def invertBinaryString(binaryString):
    return ''.join(['1' if i == '0' else '0' for i in binaryString])

# Convert binary numbers into decimal
gamma_rate = int(gamma_rate_binary, 2)
epsilon_rate = int(invertBinaryString(gamma_rate_binary), 2)

# Print the solution
print(gamma_rate * epsilon_rate)
