#!/usr/bin/env python
# coding: utf-8

from Display import *
from backward import *


if False: # Foward
    config = Configuration([Cell(5, 6), Cell(5,5), Cell(5, 7)],
                           [alive,       alive,     alive])

    Display(config).show()

if True: #Backward
    config = Configuration([Cell(5, 6), Cell(5,5), Cell(5, 7)],
                           [alive,       alive,     alive])
