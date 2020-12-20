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
            self.cells = [c for c in args[0]]
            self.states = [s for s in args[1]]
            self.default_state = args[2]
        else:
            raise Exception("bad arguments")

    def __len__(self):
        return len(self.stateList())

    def stateList(self):
        return  [self.cells, self.states]

    def stateOf(self, cell):
        """Returns the state of 'cell'."""
        if not isinstance(cell, Cell):
            raise Exception("bad type")
        for i in range(len(self.cells)):
            if self.cells[i]==cell:
                return self.states[i]
        return self.default_state
