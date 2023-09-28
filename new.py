#!/usr/bin/env python

import sys
from datetime import date
from helpers import getProblem, readFile, touchFile, writeFile

description = (
    "Generate the directories and files for a new Advent of Code problem automatically"
)
usage = f"""Usage: {sys.argv[0]} [year] [day]

[year] Must be a 4 digit integer between 2015 and the current year (inclusive),
       default is 2015
[day]  Must be an integer between 1 and 25, default is 1

Note:  If [year] is the current year, [day] cannot be a day in December that has
       not yet come to pass"""

# Parse commandline arguments
if any(h in sys.argv for h in ["help", "-help", "--help", "-h"]):
    print(f"{description}\n")
    print(usage)
    exit()

problem_date = [2015, 1]

for index, arg in enumerate(sys.argv[1:]):
    try:
        problem_date[index] = int(arg)
    except Exception:
        print(f"Invalid argument: {arg}", file=sys.stderr)
        print(usage, file=sys.stderr)
        exit(1)

year = problem_date[0]
day = problem_date[1]

# Validate year
if not (2015 <= year <= date.today().year):
    print(f"Invalid year: {year}", file=sys.stderr)
    print(usage, file=sys.stderr)
    exit(1)

# Validate day
if not (1 <= day <= (date.today().day if year == date.today().year else 25)):
    print(f"Invalid day: {day}", file=sys.stderr)
    print(usage, file=sys.stderr)
    exit(1)

# Write problem file with first part of the problem (2nd part requires authentication)
problem = getProblem(year, day)
problem_dir = f"{year}/day{day}"
writeFile(f"{problem_dir}/README.md", problem)

# Write part1.py and part2.py from template
part_template = readFile("helpers/template.py", return_type=str)
part1_file = f"{problem_dir}/part1.py"
part2_file = f"{problem_dir}/part2.py"
writeFile(part1_file, part_template, executable=True)
writeFile(part2_file, part_template, executable=True)

# Touch input.txt file (cant get content automatically yet, requires authentication)
touchFile(f"{problem_dir}/input.txt")
