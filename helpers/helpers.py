# Import required libraries
import os
import sys
import stat
import time
import fnmatch
from colorama import Fore, Style
from pathlib import Path
from urllib import request
from html2text import html2text

# Read and return content of input file as a list or a string (list is default)
def getInput(return_type=list):
    return readFile('input.txt', return_type)

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
    text_array.append('\n<details>')
    text_array.append('    <summary>Reveal the answer!</summary>')
    text_array.append('    Your puzzle answer was <code>______</code>.')
    text_array.append('</details>')
    text_array.append('\n## --- Part Two ---')
    text_array.append('\n\n\n<details>')
    text_array.append('    <summary>Reveal the answer!</summary>')
    text_array.append('    Your puzzle answer was <code>______</code>.')
    text_array.append('</details>\n')
    problem = '\n'.join(text_array).replace('\-', '-').replace('  *', '-').replace('## --- Day', '# --- Day')

    return problem

# Read a file into a list or a string (list is default)
def readFile(filepath, return_type=list):
    content = None

    try:
        with open(os.path.join(sys.path[0], filepath), 'r') as f:
            content = f.read()
    except:
        print(f'Could not read file {filepath}', file=sys.stderr)
        exit(1)

    if return_type == str:
        return content
    elif return_type == list:
        content = content.splitlines()
        return list(content[0]) if len(content) == 1 else content
    else:
        print(f'Unsupported return type for readFile method: {return_type}', file=sys.stderr)
        exit(1)

# Write content to a file and optionally make it executable
def writeFile(filepath, content, executable=False):
    filepath = os.path.join(sys.path[0], filepath)

    if os.path.exists(filepath):
        response = input(f'File {filepath} already exists. Overwrite? (y/n) [n]: ')
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

    if executable:
        makeFileExecutable(filepath)

# Touch a file
def touchFile(filepath):
    Path(filepath).touch()

# Make a file executable
def makeFileExecutable(filepath):
    try:
        st = os.stat(filepath)
        os.chmod(filepath, st.st_mode | stat.S_IEXEC)
    except:
        print(f'Unable to change permissions of file {filepath}')

# Timer decorator class with arguments (name)
class timer(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        def inner():
            print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{self.name}{Style.RESET_ALL}")

            start = time.time()
            return_value = func()
            end = time.time()

            time_to_run = end - start
            print(time_to_run, 'seconds')

            return {
                "name": self.name,
                "return_value": return_value,
                "time_to_run": time_to_run
            }

        return inner

# Compare two solution answers and runtimes
# TODO: Compare more than 2 solutions
def compare(func):
    def inner():
        solutions = func()

        solution1 = solutions[0]["return_value"]
        solution2 = solutions[1]["return_value"]

        if solution1 == solution2:
            print(f"Solutions {Fore.GREEN}match{Style.RESET_ALL}!")
        else:
            print(f"Solutions {Fore.RED}do not match{Style.RESET_ALL}.")

        solution1_time = solutions[0]['time_to_run']
        solution2_time = solutions[1]['time_to_run']
        faster_solution = solutions[int(solution1_time > solution2_time)]['name']

        print(f"The {faster_solution} solution was {'faster' if len(solutions) == 2 else 'the fastest'}.")

    return inner