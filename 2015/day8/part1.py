#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput

# Get Data
santas_list = getInput()

code_chars = sum([len(item) for item in santas_list])
memory_chars = sum(
    [len(item.encode("utf-8").decode("unicode-escape")) - 2 for item in santas_list]
)

print(code_chars - memory_chars)
