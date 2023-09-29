#!/bin/bash -e

# stop the build if there are Python syntax errors or undefined names
flake8 . --select=E9,F63,F7,F82 --extend-ignore=E203 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide.
flake8 . --extend-ignore=E203 --max-complexity=10 --max-line-length=88 --statistics
