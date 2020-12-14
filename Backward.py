#!/usr/bin/env python
# coding: utf-8

from Game import *

class Node:

    def __init__(self, configuration):
        self.configuration = Configuration
        self.children = []

    def addChild(self, configuration):
        self.children.append(configuration)
