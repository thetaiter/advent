#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput
from utils import get_number_for_hash_starting_with_zeros

# Get Data
data = getInput(return_type=str)

# Solution
print(get_number_for_hash_starting_with_zeros(data))
