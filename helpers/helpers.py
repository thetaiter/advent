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
    return readFile("input.txt", return_type)


# Automatically get the problem text from adventofcode.com
def getProblem(year=2015, day=1):
    # Get problem webpage HTML
    webpage = f"https://adventofcode.com/{year}/day/{day}"
    response = request.urlopen(webpage)
    html = response.read().decode("UTF-8")
    response.close()

    # Render and format problem text
    text = html2text(html)
    text_array = text.split("\n")
    matching = fnmatch.filter(text_array, "## *")
    first_line = text_array.index(matching[0])
    text_array = text_array[first_line:-7]
    text_array.insert(1, "\n## --- Part One ---")
    text_array.append("\n<details>")
    text_array.append("    <summary>Reveal the answer!</summary>")
    text_array.append("    Your puzzle answer was <code>______</code>.")
    text_array.append("</details>")
    text_array.append("\n## --- Part Two ---")
    text_array.append("\n\n\n<details>")
    text_array.append("    <summary>Reveal the answer!</summary>")
    text_array.append("    Your puzzle answer was <code>______</code>.")
    text_array.append("</details>\n")
    print("\n".join(text_array))
    problem = (
        "\n".join(text_array)
        .replace(r"\-", "-")
        .replace("  *", "-")
        .replace("## --- Day", "# --- Day")
    )
    print(problem)

    return problem


# Read a file into a list or a string (list is default)
def readFile(filepath, return_type=list):
    content = None

    try:
        with open(os.path.join(sys.path[0], filepath), "r") as f:
            content = f.read()
    except Exception:
        raise Exception(f"Could not read file {filepath}")

    if return_type == str:
        return content.rstrip()
    elif return_type == list:
        content = content.splitlines()
        return list(content[0]) if len(content) == 1 else content
    else:
        raise Exception(f"Unsupported return type for readFile method: {return_type}")


# Write content to a file and optionally make it executable
def writeFile(filepath, content, executable=False):
    filepath = os.path.join(sys.path[0], filepath)

    if os.path.exists(filepath):
        response = input(f"File {filepath} already exists. Overwrite? (y/n) [n]: ")
        if response.lower() != "y":
            print("Aborting.")
            exit(1)

    filedir = os.path.dirname(filepath)

    if not os.path.exists(filedir):
        os.makedirs(filedir)

    try:
        with open(filepath, "w") as f:
            f.write(content)
    except Exception:
        raise Exception(f"Could not write file {filepath}")

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
    except Exception:
        raise Exception(f"Unable to change permissions of file {filepath}")


# Decorator function for timing a given function
def timer(*args, **kwargs):
    def inner(func):
        def wrapper(*args, **kwargs):
            if name:
                print(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}{name}{Style.RESET_ALL}")

            return {"name": name, **timed_run(func, *args, **kwargs)}

        return wrapper

    if len(args) == 1 and callable(args[0]):
        name = None
        return inner(args[0])
    else:
        name = (
            args[0]
            if len(args) > 0
            else kwargs["name"]
            if "name" in kwargs.keys()
            else None
        )
        return inner


# Function to get the runtime of another function
def timed_run(func, *args, **kwargs):
    start = time.time()
    return_value = func(*args, **kwargs)
    end = time.time()
    time_to_run = end - start

    print(time_to_run, "seconds")

    return {"return_value": return_value, "time_to_run": time_to_run}


# Decorator to compare multiple solution answers and runtimes
def compare(func):
    def inner():
        solutions = func()
        solutions = (
            solutions[0]
            if isinstance(solutions, list) and len(solutions) == 1
            else solutions
        )

        if isinstance(solutions, list):
            solutions_match = (
                len(set(solution["return_value"] for solution in solutions)) == 1
            )
            match_text = f"{Fore.GREEN}match{Style.RESET_ALL}!"
            do_not_match_text = (
                f"{Fore.RED}do not match{Style.RESET_ALL}. Skipping runtime comparison."
            )

            if solutions_match:
                print(f"Solutions {match_text}")
            else:
                print(f"Solutions {do_not_match_text}")
                return None

            if any(solution["name"] is None for solution in solutions):
                print(
                    (
                        "Warning: All timers must be given names to be"
                        " compared to other timers."
                    ),
                    file=sys.stderr,
                )
                return None
            elif not len(set(solution["name"] for solution in solutions)) == len(
                solutions
            ):
                print(
                    "Warning: Cannot compare two timers with the same name.",
                    file=sys.stderr,
                )
                return None

            fastest_solution = min(solutions, key=lambda s: s["time_to_run"])
            fastest_solution_name = (
                f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}"
                f"{fastest_solution['name']}{Style.RESET_ALL}"
            )
            verbiage = "faster" if len(solutions) == 2 else "the fastest"

            print(f"The {fastest_solution_name} solution was {verbiage}.")
        elif isinstance(solutions, dict):
            fastest_solution = solutions
        else:
            raise Exception(
                f"Comparing solutions of type '{type(solutions)}' is not supported."
            )

        return fastest_solution

    return inner
