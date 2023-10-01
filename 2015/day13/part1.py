#!/usr/bin/env python

# Import helper functions included in this repository
from common import get_people, get_seating_order_happiness
from helpers import getInput

# Get Data
data = getInput()

# Solution
people = get_people(data)
total_happiness = get_seating_order_happiness(people)

print(max(total_happiness))
