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
        "distance": 0,
        "score": 0,
    }
    for line in data
]

time_limit = 2503
elapsed_time = 0

while elapsed_time < time_limit:
    for i, deer in enumerate(reindeer):
        if (elapsed_time % (deer["fly_time"] + deer["rest_time"])) < deer["fly_time"]:
            reindeer[i]["distance"] += deer["speed"]

    furthest_distance = max([deer["distance"] for deer in reindeer])
    leaders = [
        deer["name"] for deer in reindeer if deer["distance"] == furthest_distance
    ]

    for i, deer in enumerate(reindeer):
        if deer["name"] in leaders:
            reindeer[i]["score"] += 1

    elapsed_time += 1

print(max([deer["score"] for deer in reindeer]))
