#!/usr/bin/env python
# coding: utf-8

SPACE_DIMENSION = 2

class Cell :
    """Represents a cell of the grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    cell = Cell(0, 1)
