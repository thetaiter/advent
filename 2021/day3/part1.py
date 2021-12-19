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

for line in lines:
    for i, char in enumerate(line):
        if char == '0':
            zeros[i] += 1
        else:
            ones[i] += 1

for i in range(len(zeros)):
    if zeros[i] > ones[i]:
        gamma_rate_binary += '0'
    else:
        gamma_rate_binary += '1'

def invertBinaryString(binaryString):
    return ''.join(['1' if i == '0' else '0' for i in binaryString])

gamma_rate = int(gamma_rate_binary, 2)
epsilon_rate = int(invertBinaryString(gamma_rate_binary), 2)

print(gamma_rate * epsilon_rate)
