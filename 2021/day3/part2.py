#!/usr/bin/env python3

import os
import sys
import time

# Read lines of input file into an array
lines = []
with open(os.path.join(sys.path[0], 'input.txt'), 'r') as input:
   lines = input.read().splitlines()


# Recursive function to calculate oxygen generator rating
def calculate_rating(data, rating, bit=0):
    # Completion criteria has been met, return the final value
    if len(data) == 1:
        return data[0]

    ones = []
    zeroes = []

    # Calculate number of ones and zeroes for each bit
    for binary in range(len(data)):
        if data[binary][bit] == '0':
            zeroes.append(data[binary])
        else:
            ones.append(data[binary])

    # Create new data dictionary
    if len(zeroes) > len(ones):
        newData = {
            'oxygen': zeroes,
            'co2': ones
        }
    else:
        newData = {
            'oxygen': ones,
            'co2': zeroes
        }
    
    # Recurse by calling self with new data, returning the result up the call stack
    return calculate_rating(newData[rating], rating, bit+1)


# Calculate oxygen generator and cos scrubber ratings
oxygen_rating_binary = calculate_rating(lines, 'oxygen')
oxygen_rating = int(oxygen_rating_binary, 2)

co2_rating_binary = calculate_rating(lines, 'co2')
co2_rating = int(co2_rating_binary, 2)

# Print the solution
print(oxygen_rating * co2_rating)
