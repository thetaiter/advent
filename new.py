#!/usr/bin/env python

import sys
from helpers import *

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
problem_dir = f'{year}/day{day}'
writeFile(f'{problem_dir}/problem.md', problem)

# Write part1.py from template
part_template = readFile('helpers/template.py', string=True)
part_filename = f'{problem_dir}/part1.py'
writeFile(part_filename, part_template)
makeFileExecutable(part_filename)

# Touch input.txt file (cannot get it automatically... yet)
touchFile(f'{problem_dir}/input.txt')
