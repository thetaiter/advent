#!/usr/bin/env python

# Import helper functions included in this repository
from common import update_lights
from helpers import getInput

# Get Data
instructions = getInput()


# Solution
def update_light_state(action: str, light: int):
    if action == "on":
        return light + 1
    elif action == "off":
        return max(light - 1, 0)
    elif action == "toggle":
        return light + 2


num_lights_on = update_lights(1000, instructions, update_light_state)

print(num_lights_on)
