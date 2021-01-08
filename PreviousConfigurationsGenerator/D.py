#!/usr/bin/env python
# coding: utf-8

import random
from Configuration import *
from Forward import *

def dunstan(game):
    def aux(configuration):
        next = Forward(configuration, game).nextConfiguration
        print("Search for previous configuration", end="")
        cells = [c.copy() for c in configuration.cells]
        for c in configuration.cells:
            for v in game.voisin(c):
                if v not in cells:
                    cells.append(v)
        l = []
        while len(l)!=5:
            print(".", end="")
            states = []
            for c in cells:
                states.append(game.base[random.randint(0, len(game.base)-1)])
            prev_conf = Configuration(cells, states, configuration.default_state)
            if next(prev_conf) == configuration:
                l.append(prev_conf)
        print(".")
        return l
    return aux
