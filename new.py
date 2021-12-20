#!/usr/bin/env python

import sys
from helpers import getProblem, readFile, writeFile, touchFile

# Grab arguments from commandline
try:
    year = int(sys.argv[1])
except:
    year = 2015

try:
    day = int(sys.argv[2])
except:
    day = 1

# Write problem file with first part of the problem
problem = getProblem(year, day)
writeFile(f'{year}/day{day}/problem.md', problem)

# Write part1.py from template
part_template = '\n'.join(readFile('helpers/template.py'))
writeFile(f'{year}/day{day}/part1.py', part_template)

# Touch input.txt file (cannot get it automatically... yet)
touchFile(f'{year}/day{day}/input.txt')
