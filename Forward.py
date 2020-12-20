#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot
import numpy
from Game import *

class Forward:
    """Allow to display configurations and their evolutions."""

    def __init__(self, configuration, game):
        if not isinstance(configuration, Configuration):
            raise Exception("bad arguments")
        self.game = game
        self.configs = [configuration]
        self.time = 0
        self.fig, self.ax = matplotlib.pyplot.subplots(1)

        cid = self.fig.canvas.mpl_connect('key_press_event', self.onPress)
        self.plot()

    def nextConfiguration(self, configuration):
        """Returns the next configuration."""
        old_cells = configuration.stateList()[0]
        old_states = configuration.stateList()[1]
        new_cells = [c for c in old_cells]
        new_states = []
        for i in range(len(old_cells)) :
            for v in self.game.voisin(old_cells[i]):
                if not v in new_cells :
                    new_cells.append(v)
        for j in new_cells :
            neighboors = [0 for i in range(len(self.game.base))]
            for v in self.game.voisin(j):
                neighboors[self.game.base.index(configuration.stateOf(v))] += 1
            new_states.append(self.game.image(configuration.stateOf(j),
                                         neighboors))
        cells = []
        states = []
        for l in range(len(new_states)):
            if new_states[l] != configuration.default_state :
                cells.append(new_cells[l])
                states.append(new_states[l])
        return Configuration(cells, states, configuration.default_state)


    def onPress(self, event):
        if event.key=="right":
            self.time += 1
        elif event.key=="left" and self.time!=0:
            self.time -= 1
        if self.time==len(self.configs):
            print('Generating configuration t='+str(self.time))
            self.configs.append(self.nextConfiguration(self.configs[-1]))
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
            x = configuration.cells[i][0]
            y = configuration.cells[i][1]
            state = configuration.states[i]
            circ = matplotlib.pyplot.Circle((x, y), 0.5, color=state.color)
            self.ax.add_patch(circ)
        matplotlib.pyplot.show()

    def show(self):
        matplotlib.pyplot.show()
