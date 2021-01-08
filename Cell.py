#!/usr/bin/env python
# coding: utf-8

SPACE_DIMENSION = 2

class Cell :
    """Represents a cell of the grid."""

    def __init__(self, *args):
        self.coordinates = args

    def __getitem__(self, index):
        return self.coordinates[index]

    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise Exception("value must be an integer")
        self.coordinates[index] = value

    def __len__(self):
        return len(self.coordinates)

    def __eq__(self, c):
        """Returns true if the cells have the same position."""
        for i in range(SPACE_DIMENSION):
            if self[i]!=c[i]:
                return False
        return True

    def __str__(self):
        return "["+"; ".join([str(self[i]) for i in range(len(self))])+"]"

    def copy(self):
        return Cell(*self.coordinates)
