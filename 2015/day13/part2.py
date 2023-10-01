#!/usr/bin/env python

# Import helper functions included in this repository
from common import get_people, get_seating_order_happiness
from helpers import getInput

# Get Data
data = getInput()

# Solution
people = get_people(data)

for i, person in enumerate(people):
    people[i]["happiness"]["Me"] = 0

people.append(
    {
        "name": "Me",
        "happiness": {person["name"]: 0 for person in people if person["name"] != "Me"},
    }
)

total_happiness = get_seating_order_happiness(people)

print(max(total_happiness))
