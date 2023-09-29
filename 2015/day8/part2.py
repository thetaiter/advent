#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
santas_list = getInput()

code_chars = sum([len(item) for item in santas_list])
string_chars = sum([len(repr(item).replace('"', '""')) for item in santas_list])

print(string_chars - code_chars)
