#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot
import numpy
from Game import *

class Forward:
    """Allow to display configurations and their evolutions."""

    screenshot = "t"
    resize = "r"
    forward = "right"
    backward = "left"

    def __init__(self, configuration, game):
        if not isinstance(configuration, Configuration):
            raise Exception("bad arguments")
        if not isinstance(game, Game):
            raise Exception("bad arguments")
        self.game = game
        self.configs = [configuration]
        self.time = 0
        self.fig, self.ax = matplotlib.pyplot.subplots(1)
        self.x_min = -10
        self.y_min = -10
        self.x_max = 10
        self.y_max = 10
        cid = self.fig.canvas.mpl_connect('key_press_event', self.onPress)

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

    def size(self, configuration):
        x_min, x_max = float('inf'), -float('inf')
        y_min, y_max = float('inf'), -float('inf')
        for c in configuration.cells:
            x_max = max(c[0], x_max)
            x_min = min(c[0], x_min)
            y_max = max(c[1], y_max)
            y_min = min(c[1], y_min)
        x_center = int((x_max+x_min)/2)
        y_center = int((y_max+y_min)/2)
        scope = max(x_max-x_min, y_max-y_min)
        print("Resizing")
        self.x_max = x_center + scope
        self.x_min = x_center - scope
        self.y_max = y_center + scope
        self.y_min = y_center - scope

    def onPress(self, event):
        if event.key==Forward.forward: # forward
            self.time += 1
        elif event.key==Forward.backward and self.time!=0: # backward
            self.time -= 1
        elif event.key==Forward.resize: # resize
            self.size(self.configs[self.time])
        elif event.key==Forward.screenshot:
            print("Screenshot")
            matplotlib.pyplot.savefig("Screenshots/"+str(self.time)+'.pdf')
        if self.time==len(self.configs):
            print('Generating configuration t='+str(self.time))
            self.configs.append(self.nextConfiguration(self.configs[-1]))
        self.plot()

    def plot(self):
        matplotlib.pyplot.cla()
        self.ax.set_title('t='+str(self.time))
        configuration = self.configs[self.time]
        self.ax.set_xlim(self.x_min, self.x_max)
        self.ax.set_ylim(self.y_min, self.y_max)
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
