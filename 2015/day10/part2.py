#!/usr/bin/env python

# Import helper functions included in this repository
from common import get_sequence
from helpers import getInput

# Get Data
data = getInput(return_type=str)

print(len(get_sequence(data, 50)))
