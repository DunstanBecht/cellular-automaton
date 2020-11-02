#!/usr/bin/env python
# coding: utf-8

from Game import *
from Display import *

config = Configuration([Cell(0, -1), Cell(0,0), Cell(0, 1)],
                       [alive,       alive,     alive])

print(config.stateOf(Cell(0, -1)))

display(config)
