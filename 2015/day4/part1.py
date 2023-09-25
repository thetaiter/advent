#!/usr/bin/env python

# Import helper functions included in this repository
from hashlib import md5
from helpers import getInput

# Get Data
data = getInput(return_type=str)

# Solution
md5_hex = ""
number = 0
zeros = 5

while md5_hex[:zeros] != zeros * "0":
    number += 1
    md5_hex = md5(f"{data}{number}".encode("utf-8")).hexdigest()

print(number)
