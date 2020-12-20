#!/usr/bin/env python
# coding: utf-8

from Game import *
from PreviousConfigurationsGenerator import J
from ObjectivesFunctions import J

class Node:

    def __init__(self, configuration):
        self.configuration = Configuration
        self.children = []

    def addChild(self, configuration):
        self.children.append(configuration)

class Backward:

    def __init__(self, configuration):
        self.tree = Node(configuration)
