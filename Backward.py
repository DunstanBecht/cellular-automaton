#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot
import numpy
from Game import *
from PreviousConfigurationsGenerator import J
from ObjectivesFunctions import J
from PreviousConfigurationsGenerator import D

class Node:

    def __init__(self, configuration, parent=None):
        if not isinstance(configuration, Configuration):
            raise Exception("bad arguments")
        if parent is not None and not isinstance(parent, Node):
            raise Exception("bad arguments")
        self.configuration = configuration
        self.children = []
        self.parent = parent

    def addChild(self, configuration):
        if not isinstance(configuration, Configuration):
            raise Exception("bad arguments")
        node = Node(configuration, self)
        self.children.append(node)

class Backward:

    screenshot = "t"
    resize = "r"
    forward = "left"
    backward = "right"
    up = "up"
    down = "down"

    def __init__(self, configuration, previousConfiguration):
        if not isinstance(configuration, Configuration):
            raise Exception("bad arguments")
        self.previousConfiguration = previousConfiguration
        self.time = 0
        self.current_node = Node(configuration)
        self.fig, self.ax = matplotlib.pyplot.subplots(1)
        self.x_min = -10
        self.y_min = -10
        self.x_max = 10
        self.y_max = 10
        cid = self.fig.canvas.mpl_connect('key_press_event', self.onPress)

    def plot(self):
        matplotlib.pyplot.cla()
        if self.current_node.parent != None:
            child = self.current_node.parent.children.index(self.current_node)
        else:
            child = 0
        self.ax.set_title('t='+str(self.time)+' / child: '+str(child))
        configuration = self.current_node.configuration
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

    def onPress(self, event):
        if event.key==Backward.backward: # backward
            if len(self.current_node.children)==0:
                children = self.previousConfiguration(self.current_node.configuration)
                for child in children:
                    self.current_node.addChild(child)
            self.current_node = self.current_node.children[0]
            self.time -= 1
        elif event.key==Backward.forward and self.time!=0: # forward
            self.current_node = self.current_node.parent
            self.time += 1
        elif event.key==Backward.up: # forward
            if self.current_node.parent != None:
                child = self.current_node.parent.children.index(self.current_node)
                self.current_node = self.current_node.parent.children[(child+1)%len(self.current_node.parent.children)]
        elif event.key==Backward.down: # forward
            if self.current_node.parent != None:
                child = self.current_node.parent.children.index(self.current_node)
                self.current_node = self.current_node.parent.children[(child-1)%len(self.current_node.parent.children)]
        elif event.key==Backward.size: # resize
            self.size(self.configs[self.time])
        elif event.key==Backward.screenshot:
            print("Screenshot")
            matplotlib.pyplot.savefig("Screenshots/"+str(self.time)+'.pdf')
        self.plot()

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
