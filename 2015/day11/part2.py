#!/usr/bin/env python

# Import helper functions included in this repository
from common import get_next_password
from helpers import getInput

# Get Data
current_password = getInput(return_type=str)

next_password = get_next_password(current_password)
print(get_next_password(next_password))
