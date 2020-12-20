#!/usr/bin/env python
# coding: utf-8

class State:
    """Represents a state that can be taken by a cell."""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name

alive = State("alive", "black")
dead = State("dead", "white")
