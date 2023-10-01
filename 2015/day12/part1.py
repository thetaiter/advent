#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
data = getInput(filename="input.json")


# Solution
def get_numbers(obj):
    if isinstance(obj, int):
        return [obj]
    elif isinstance(obj, list):
        return [num for item in obj for num in get_numbers(item)]
    elif isinstance(obj, dict):
        return [num for key in obj for num in get_numbers(obj[key])]
    else:
        return []


print(sum(get_numbers(data)))
