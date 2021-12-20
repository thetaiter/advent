# Advent of Code

## Setup

All programming challenges come from [Advent of Code](https://adventofcode.com/).

I used `Conda` to set up a clean `python 3.10` environment. Installation instructions on how to do that can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). Once Conda is installed, follow these steps in the root of this repository to get started:

1. `conda create --name advent python=3.10`
2. `conda activate advent`
3. `pip install -e helpers`

And then you can run the challenge solutions like this:<br>
`./<year>/day<#>/part<#>.py` <br> OR <br> `python3 ./<year>/day<#>/part<#>.py`

You can have your conda environment change to advent automatically when you cd into this repository using `direnv`. You can follow the instructions [here](https://medium.com/@manishdixit1986/auto-switch-conda-env-per-directory-using-conda-direnv-in-linux-13c912da6520) for instructions on how to set that up.