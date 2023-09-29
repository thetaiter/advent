#!/usr/bin/env python

# Import helper functions included in this repository
from common import get_wire_signals
from helpers import getInput

# Get Data
instructions = getInput()

# Solution
print(get_wire_signals(instructions)["a"])
