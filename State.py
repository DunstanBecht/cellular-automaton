#!/usr/bin/env python
# coding: utf-8

class State:
    """Represents a possible state of a cell."""
    
    def __init__(self, name):
        self.name = name

alive = State("alive")
dead = State("dead")

if __name__ == "__main__":
    print(isinstance(alive, State))
