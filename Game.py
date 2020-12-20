#!/usr/bin/env python
# coding: utf-8

from Configuration import *

class Game:
    """Defines the rules of a game."""

    def __init__(self, base, matrix):
        """ Msij gives the next state for a cell in a state s with i neighboors in the first state of the base, j in the second state, and so on. """
        self.base = base
        self.matrix= matrix

    def image(self, state, neighboors):
        """Gives a state."""
        if sum(neighboors)!=8:
            raise Exception("wrong arguments")

        state = self.matrix[self.base.index(state)]
        for i in neighboors:
            state = state[i]
        return state

    def preImage(self, state):
        """ """
        return [[]]

    def voisin(self, cell):
        c1 = Cell(cell[0]+1, cell[1]+1)
        c2 = Cell(cell[0]+1, cell[1]-1)
        c3 = Cell(cell[0]-1, cell[1]+1)
        c4 = Cell(cell[0]-1, cell[1]-1)
        c5 = Cell(cell[0]+1, cell[1])
        c6 = Cell(cell[0]-1, cell[1])
        c7 = Cell(cell[0], cell[1]+1)
        c8 = Cell(cell[0], cell[1]-1)
        return [c1, c2, c3, c4, c5, c6, c7, c8]

game_of_life = Game([alive, dead], 
                    [[[None, None, None, None, None, None, None, None, dead],
                      [None, None, None, None, None, None, None, dead, None],
                      [None, None, None, None, None, None, alive, None, None],
                      [None, None, None, None, None, alive, None, None, None],
                      [None, None, None, None, dead, None, None, None, None],
                      [None, None, None, dead, None, None, None, None, None],
                      [None, None, dead, None, None, None, None, None, None],
                      [None, dead, None, None, None, None, None, None, None],
                      [dead, None, None, None, None, None, None, None, None]],
                     [[None, None, None, None, None, None, None, None, dead],
                      [None, None, None, None, None, None, None, dead, None],
                      [None, None, None, None, None, None, dead, None, None],
                      [None, None, None, None, None, alive, None, None, None],
                      [None, None, None, None, dead, None, None, None, None],
                      [None, None, None, dead, None, None, None, None, None],
                      [None, None, dead, None, None, None, None, None, None],
                      [None, dead, None, None, None, None, None, None, None],
                      [dead, None, None, None, None, None, None, None, None]]])
