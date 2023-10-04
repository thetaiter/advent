#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
data = getInput()

# Solution
reindeer = [
    {
        "name": line.split()[0],
        "speed": int(line.split()[3]),
        "fly_time": int(line.split()[6]),
        "rest_time": int(line.split()[13]),
    }
    for line in data
]

time_limit = 2503
distances = []

for deer in reindeer:
    remainder = time_limit % (deer["fly_time"] + deer["rest_time"])
    distance = (
        int(time_limit / (deer["fly_time"] + deer["rest_time"]))
        * deer["speed"]
        * deer["fly_time"]
    ) + (
        deer["speed"] * deer["fly_time"]
        if remainder >= deer["fly_time"]
        else deer["speed"] * remainder
    )

    distances.append(distance)

print(max(distances))
