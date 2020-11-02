#!/usr/bin/env python
# coding: utf-8

SPACE_DIMENSION = 2

class Cell :
    """Represents a cell of the grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, c):
        """Returns true if the cells have the same position."""
        return self.x==c.x and self.y==c.y

    def __str__(self):
        return "["+str(self.x)+", "+str(self.y)+"]"

if __name__ == "__main__":
    cell = Cell(0, 1)
    print(cell)
