# Import required libraries
import os
import sys
import stat
import fnmatch
from pathlib import Path
from urllib import request
from html2text import html2text

# Read and return content of input file as a list (unless there is onyly one line)
def getInput():
    return readFile('input.txt')

# Automatically get the problem text from adventofcode.com
def getProblem(year=2015, day=1):
    # Get problem webpage HTML
    webpage = f'https://adventofcode.com/{year}/day/{day}'
    response = request.urlopen(webpage)
    html = response.read().decode('UTF-8')
    response.close()

    # Render and format problem text
    text = html2text(html)
    text_array = text.split('\n')
    matching = fnmatch.filter(text_array, '## *')
    first_line = text_array.index(matching[0])
    text_array = text_array[first_line:-7]
    text_array.insert(1,'\n## --- Part One ---')
    text_array.append('\nYour puzzle answer was ______.\n')
    text_array.append('\n## --- Part Two ---\n\n\nYour puzzle answer was ______.\n')
    problem = '\n'.join(text_array).replace('\-', '-').replace('  *', '-').replace('## --- Day', '# --- Day')

    return problem

# Read a file  at a relative path into a list
def readFile(relative_path):
    content = None
    try:
        with open(os.path.join(sys.path[0], relative_path), 'r') as f:
            content = f.read().splitlines()
    except:
        print(f'Could not read file {relative_path}', file=sys.stderr)
        exit(1)

    return content[0] if content and len(content) == 1 else content

# Write content to a file at a relative path
def writeFile(relative_path, content):
    filepath = os.path.join(sys.path[0], relative_path)

    if os.path.exists(filepath):
        response = input(f'File {relative_path} already exists. Overwrite? (y/n) [n]: ')
        if response.lower() != 'y':
            print('Aborting.', file=sys.stderr)
            exit(1)

    filedir = os.path.dirname(filepath)

    if not os.path.exists(filedir):
        os.makedirs(filedir)

    try:
        with open(filepath, 'w') as f:
            f.write(content)
    except:
        print(f'Could not write file {filepath}', file=sys.stderr)
        exit(1)

# Touch a file at a relative path
def touchFile(relative_path):
    Path(relative_path).touch()

# Make a file executable
def makeFileExecutable(relative_path):
    st = os.stat(relative_path)
    os.chmod(relative_path, st.st_mode | stat.S_IEXEC)
