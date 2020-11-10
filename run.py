#!/usr/bin/env python
# coding: utf-8

from Game import *
from Display import *

config = Configuration([Cell(5, 6), Cell(5,5), Cell(5, 7)],
                       [alive,       alive,     alive])

print(config.stateOf(Cell(0, -1)))

display(config)
