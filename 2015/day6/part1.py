#!/usr/bin/env python

# Import helper functions included in this repository
from common import update_lights
from helpers import getInput

# Get Data
instructions = getInput()


# Solution
def update_light_state(action: str, light: int):
    if action == "toggle":
        return int(not light)
    else:
        return int(action == "on")


num_lights_on = update_lights(1000, instructions, update_light_state)

print(num_lights_on)
