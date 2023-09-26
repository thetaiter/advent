#!/usr/bin/env python

# Import helper functions included in this repository
from helpers import getInput
from utils import BingoGame

# Get Data
data = getInput()

# Run the game
game = BingoGame(data)
game.play()
