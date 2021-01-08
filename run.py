#!/usr/bin/env python
# coding: utf-8

from Forward import *
from Backward import *


if True: # Foward
    print("Press '"+Forward.forward+"' to move forward.")
    print("Press '"+Forward.backward+"' to move backward.")
    print("Press '"+Forward.resize+"' to resize the viewbox.")
    print("Press '"+Forward.screenshot+"' to take a screenshot.")

    glider_mess = [
                   Cell( 0, 1),
                   Cell( 1, 2),
                   Cell( 2, 0),
                   Cell( 2, 1),
                   Cell( 2, 2),
                   Cell( 9, 4),
                   Cell(10, 4),
                   Cell(10, 5),
                   Cell(11, 3),
                   Cell(11, 5),
                  ]

    cells = glider_mess
    states = [alive for c in cells]
    config = Configuration(cells, states, dead)

    Forward(config, game_of_life).plot()

if F: #Backward
    print("Press '"+Backward.forward+"' to move forward.")
    print("Press '"+Backward.backward+"' to move backward.")
    print("Press '"+Backward.up+"' to move up on the same tree level.")
    print("Press '"+Backward.down+"' to move up on the same tree level.")
    print("Press '"+Backward.resize+"' to resize the viewbox.")
    print("Press '"+Backward.screenshot+"' to take a screenshot.")

    origine = [
               Cell( 0, 0),
              ]


    cells = origine
    states = [alive for c in cells]
    config = Configuration(cells, states, dead)


    Backward(config, D.dunstan(game_of_life)).plot()
