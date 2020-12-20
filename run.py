#!/usr/bin/env python
# coding: utf-8

from Forward import *
from Backward import *


if True: # Foward
    config = Configuration([Cell(5, 6), Cell(5,5), Cell(5, 7)],
                           [alive,       alive,     alive],
                           dead)

    Forward(config, game_of_life).show()

if False: #Backward
    config = Configuration([Cell(5, 6), Cell(5,5), Cell(5, 7)],
                           [alive,       alive,     alive],
                           dead)
