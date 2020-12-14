#!/usr/bin/env python
# coding: utf-8

from Cell import *
from State import *

class Configuration:
    """Represents a state of the grid (the state of each cell)."""

    default_state = dead # for undeclared cell states in __init__

    def __init__(self, *args):
        """Declares the cell states."""

        # Case 1: args = [[cell_1, cell_2, ...], [state_1, state_2, ...]]
        if len(args)==2:
            # Arguments check:
            if not isinstance(args[0], list):
                raise Exception("bad arguments")
            if not isinstance(args[1], list):
                raise Exception("bad arguments")
            if len(args[0])!=len(args[1]):
                raise Exception("bad arguments")
            for i in range(len(args[0])):
                if not isinstance(args[0][i], Cell):
                    raise Exception("bad arguments")
                if not isinstance(args[1][i], State):
                    raise Exception("bad arguments")
            # Data processing:
            self.cells = [c for c in args[0]]
            self.states = [s for s in args[1]]

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
        return Configuration.default_state

if __name__ == "__main__":
    c = Configuration([Cell(0,0)], [alive])
    print(c.nextConfiguration().stateList())
