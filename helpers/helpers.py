import os
import sys

# Read lines of input file into an array
def getInput():
    lines = []

    try:
        with open(os.path.join(sys.path[0], 'input.txt'), 'r') as input:
            lines = input.read().splitlines()
    except:
        print("Could not read data file.")
        exit(1)

    return lines
