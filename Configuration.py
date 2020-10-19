#!/usr/bin/env python
# coding: utf-8

from Cell import *
from State import *

class Configuration:
    """Represents a state of the grid (the state of each cell)."""

    def __init__(self, *args):
        pass

    def isOfState(self, state, cell):
        """Return true if the cell is alive in the configuration."""
        assert isinstance(cell, Cell)
        return True
    
    def nextState(self):
        return state
        
if __name__ == "__main__":
    pass
