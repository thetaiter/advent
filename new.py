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

# Write problem file with first part of the problem (2nd part requires authentication)
problem = getProblem(year, day)
problem_dir = f'{year}/day{day}'
writeFile(f'{problem_dir}/README.md', problem)

# Write part1.py from template
part_template = readFile('helpers/template.py', return_type=str)
part1_file = f'{problem_dir}/part1.py'
part2_file = f'{problem_dir}/part2.py'
writeFile(part1_file, part_template, executable=True)
writeFile(part2_file, part_template, executable=True)

# Touch input.txt file (cannot get it automatically... yet. It requires authentication)
touchFile(f'{problem_dir}/input.txt')
