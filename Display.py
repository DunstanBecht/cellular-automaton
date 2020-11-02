#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot
import numpy
from Configuration import *

def display(configuration):
    matplotlib.pyplot.cla()
    matplotlib.pyplot.axis('off')

    chessboard = numpy.zeros((10, 10))
    for i in range(len(configuration.cells)):
        x = configuration.cells[i].x
        y = configuration.cells[i].y
        state = configuration.states[i]
        chessboard[x, y] = 1

    matplotlib.pyplot.imshow(chessboard, cmap='binary')
    matplotlib.pyplot.show()
