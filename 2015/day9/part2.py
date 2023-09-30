#!/usr/bin/env python

# Import helper functions included in this repository
from common import get_total_distances
from helpers import getInput

# Get Data
data = getInput()

print(max(get_total_distances(data)))
