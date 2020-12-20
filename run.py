#!/usr/bin/env python
# coding: utf-8

from Forward import *
from Backward import *


if True: # Foward

    glider_mess = [Cell( 0, 1),
                   Cell( 1, 2),
                   Cell( 2, 0),
                   Cell( 2, 1),
                   Cell( 2, 2),
                   Cell( 9, 4),
                   Cell(10, 4),
                   Cell(10, 5),
                   Cell(11, 3),
                   Cell(11, 5)]

    cells = glider_mess
    states = [alive for c in cells]
    config = Configuration(cells, states, dead)

    Forward(config, game_of_life).show()

if False: #Backward
    config = Configuration([Cell(5, 6), Cell(5,5), Cell(5, 7)],
                           [alive,       alive,     alive],
                           dead)
