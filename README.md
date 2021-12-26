# Advent of Code

## Setup

All programming challenges come from [Advent of Code](https://adventofcode.com/).

I used `Conda` to set up a clean `python 3.10.0` environment. Instructions to install Conda can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). Once Conda is installed, follow these steps in the root of this repository to get started:

1. `conda create --name advent python=3.10.0`
2. `conda activate advent`
3. `pip install -r requirements.txt`
4. `pip install -e helpers`

And then you can run the challenge solutions like this:\
`./<year>/day<#>/part<#>.py`\
OR\
`python3 ./<year>/day<#>/part<#>.py`

One of my primary goals when I am solving these puzzles is to not use any extra python libraries that may make the puzzles easier to solve. I want to expose the algorithms using raw python rather than using pre-built library functions to hide the more complex logic behind the algorithms or to reduce the number of lines of code. The only libraries I do use are the `helpers` library included in this repository (to load input from the `input.txt` files) and the `time` library, in cases where there are two distinct ways of solving a puzzle and I want to compare which is faster.

You can run all challenge solutions and automatically compare the results with the answers defined in the relevant `README.md` files by running `./test.sh`. This script assumes that the first line printed from each challenge solution is the answer for that particular challenge.

You can easily set up a new challenge problem directory and files using `new.py`. Try `./new.py --help` for more information about how to use the script.

You can have your Conda environment change to `advent` automatically when you `cd` into the directory where you have this repository by using `direnv`. After installing `direnv` [here](https://direnv.net/docs/installation.html), you can follow the instructions [here](https://medium.com/@manishdixit1986/auto-switch-conda-env-per-directory-using-conda-direnv-in-linux-13c912da6520) to set that up.
