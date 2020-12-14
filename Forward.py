#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot
import numpy
from Game import *

game = GameOfLife

class Forward:
    """Allow to display configurations and their evolutions."""

    def __init__(self, configuration):
        if not isinstance(configuration, Configuration):
            raise Exception("bad arguments")
        self.configs = [configuration]
        self.time = 0
        self.fig, self.ax = matplotlib.pyplot.subplots(1)

        cid = self.fig.canvas.mpl_connect('key_press_event', self.onPress)
        self.plot()

    def onPress(self, event):
        if event.key=="right":
            self.time += 1
        elif event.key=="left" and self.time!=0:
            self.time -= 1
        if self.time==len(self.configs):
            print('Generating configuration t='+str(self.time))
            self.configs.append(self.configs[-1].nextConfiguration(game))
        self.plot()

    def plot(self):
        matplotlib.pyplot.cla()
        self.ax.set_title('t='+str(self.time))
        configuration = self.configs[self.time]
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_aspect('equal', 'box')
        matplotlib.pyplot.axis('off')
        chessboard = numpy.zeros((10, 10))
        for i in range(len(configuration.cells)):
            x = configuration.cells[i].x
            y = configuration.cells[i].y
            state = configuration.states[i]
            circ = matplotlib.pyplot.Circle((x, y), 0.5, color=state.color)
            self.ax.add_patch(circ)
        matplotlib.pyplot.show()

    def show(self):
        matplotlib.pyplot.show()

    def nextState(cell,config):
        if config.stateOf(cell) == alive :
            compteur = 0
            for i in range(len(GameOfLife.voisin(cell))):
               if config.stateOf(GameOfLife.voisin(cell)[i]) == alive :
                   compteur += 1
            if compteur == 2 or compteur == 3 :
                return alive
            else :
                return dead
        else :
            compteur2 = 0
            for i in range(len(GameOfLife.voisin(cell))) :
                if config.stateOf(GameOfLife.voisin(cell)[i]) == alive :
                    compteur2 += 1
            if compteur2 == 3 :
                return alive
            else :
                return dead


        return True
