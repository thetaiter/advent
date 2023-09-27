#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
santas_list = getInput()

def is_nice(item):
    two_pair = False
    for i in range(len(item)-1):
        pair = item[i:i+2]

        for j in range(len(item)-1):
            if j != i-1 and j != i and j != i+1 and item[j:j+2] == pair:
                two_pair = True
                break
        
        if two_pair:
            break
    
    return two_pair and any(item[i] == item[i+2] for i in range(len(item)-2))

print(len(list(filter(is_nice, santas_list))))
 