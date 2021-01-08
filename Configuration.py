#!/usr/bin/env python
# coding: utf-8

from Cell import *
from State import *

class Configuration:
    """Represents a state of the grid (gives the state of each cell)."""

    def __init__(self, *args):
        """Declares the cell states."""

        # Case 1: args = [[cell_1, cell_2, ...], [state_1, state_2, ...], default_state]
        if len(args)==3:
            # Arguments check:
            if not isinstance(args[0], list):
                raise Exception("bad arguments 1")
            if not isinstance(args[1], list):
                raise Exception("bad arguments 2")
            if len(args[0])!=len(args[1]):
                raise Exception("bad arguments 3")
            for i in range(len(args[0])):
                if not isinstance(args[0][i], Cell):
                    raise Exception("bad arguments 4")
                if not isinstance(args[1][i], State):
                    raise Exception("bad arguments 5")
            # Data processing:
            self.cells = []
            self.states = []
            self.default_state = args[2]
            for i in range(len(args[0])):
                if args[1][i]!=self.default_state:
                    self.cells.append(args[0][i])
                    self.states.append(args[1][i])

        else:
            raise Exception("bad arguments")

    def __len__(self):
        return len(self.stateList())

    def stateList(self):
        return  [self.cells, self.states]

    def __eq__(self, configuration):
        l1 = self.stateList()
        l2 = configuration.stateList()
        for l in [l1, l2]:
            for c in l[0]:
                if self.stateOf(c) != configuration.stateOf(c):
                    return False
        return True

    def stateOf(self, cell):
        """Returns the state of 'cell'."""
        if not isinstance(cell, Cell):
            raise Exception("bad type")
        for i in range(len(self.cells)):
            if self.cells[i]==cell:
                return self.states[i]
        return self.default_state

    def copy(self):
        cells = [c.copy() for c in self.cells]
        states = [s for s in self.states]
        return Configuration(cells, states, self.default_state)
