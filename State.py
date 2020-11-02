#!/usr/bin/env python
# coding: utf-8

class State:
    """Represents a possible state for the cells."""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name

alive = State("alive", "black")
dead = State("dead", "white")

if __name__ == "__main__":
    print(isinstance(alive, State))
