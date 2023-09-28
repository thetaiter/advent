#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
data = getInput()


# Recursive function to calculate oxygen generator rating
def calculate_rating(binaryData, rating, bit=0):
    # Completion criteria has been met, return the final value
    if len(binaryData) == 1:
        return binaryData[0]

    # Initialize arrays
    ones = []
    zeroes = []

    # Calculate number of ones and zeroes for each bit
    for binary in range(len(binaryData)):
        if binaryData[binary][bit] == "0":
            zeroes.append(binaryData[binary])
        else:
            ones.append(binaryData[binary])

    # Create new data dictionary
    newData = {}
    if len(zeroes) > len(ones):
        newData = {"oxygen": zeroes, "co2": ones}
    else:
        newData = {"oxygen": ones, "co2": zeroes}

    # Recurse by calling self with new data, returning the result up the call stack
    return calculate_rating(newData[rating], rating, bit + 1)


# Calculate oxygen generator and cos scrubber ratings
oxygen_rating_binary = calculate_rating(data, "oxygen")
oxygen_rating = int(oxygen_rating_binary, 2)

co2_rating_binary = calculate_rating(data, "co2")
co2_rating = int(co2_rating_binary, 2)

# Print the solution
print(oxygen_rating * co2_rating)
