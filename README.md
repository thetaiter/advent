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

You can have your Conda environment change to `advent` automatically when you `cd` into the directory where you have this repository by using `direnv`. After installing `direnv` [here](https://direnv.net/docs/installation.html), you can follow the instructions [here](https://medium.com/@manishdixit1986/auto-switch-conda-env-per-directory-using-conda-direnv-in-linux-13c912da6520) to set that up.
