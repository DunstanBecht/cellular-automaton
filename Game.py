#!/usr/bin/env python
# coding: utf-8

from Configuration import *

class Game:
    """Defines the rules."""

    def __init__(self, base, matrix):
        """ Msij gives the next state for a cell in a state s with i neighboors in the first state of the base, j in the second state, and so on. """
        self.base = base
        self.matrix= matrix

    def image(self, state, neighboors):
        """Gives a state."""
        if sum(neighboors)!=8:
            raise Exception("wrong arguments")

        state = self.matrix[self.base.index(state)]
        for i in neighboors:
            state = state[i]
        return state

    def preImage(self, state):
        """ """
        return [[]]

    def voisin(cell):
        c1 = Cell(cell.x+1, cell.y+1)
        c2 = Cell(cell.x+1, cell.y-1)
        c3 = Cell(cell.x-1, cell.y+1)
        c4 = Cell(cell.x-1, cell.y-1)
        c5 = Cell(cell.x+1, cell.y)
        c6 = Cell(cell.x-1, cell.y)
        c7 = Cell(cell.x, cell.y+1)
        c8 = Cell(cell.x, cell.y-1)
        return [c1, c2, c3, c4, c5, c6, c7, c8]

    def nextConfiguration(self, Game):
        """Returns the next configuration."""
        old_cells = self.stateList()[0]
        old_states = self.stateList()[1]
        new_cells = [c for c in old_cells]
        new_states = []
        for i in range(len(old_cells)) :
            for v in Game.voisin(old_cells[i]):
                if not v in new_cells :
                    new_cells.append(v)
        for j in new_cells :
            new_states.append(Game.nextState(j, self))
        cells = []
        states = []
        for l in range(len(new_states)):
            if new_states[l] != Configuration.default_state :
                cells.append(new_cells[l])
                states.append(new_states[l])
        return Configuration(cells, states)
        
base = [alive, dead]
matrix = [[[None, None, None, None, None, None, None, None, dead],
           [None, None, None, None, None, None, None, dead, None],
           [None, None, None, None, None, None, alive, None, None],
           [None, None, None, None, None, alive, None, None, None],
           [None, None, None, None, dead, None, None, None, None],
           [None, None, None, dead, None, None, None, None, None],
           [None, None, dead, None, None, None, None, None, None],
           [None, dead, None, None, None, None, None, None, None],
           [dead, None, None, None, None, None, None, None, None]],
          [[None, None, None, None, None, None, None, None, dead],
           [None, None, None, None, None, None, None, dead, None],
           [None, None, None, None, None, None, dead, None, None],
           [None, None, None, None, None, alive, None, None, None],
           [None, None, None, None, dead, None, None, None, None],
           [None, None, None, dead, None, None, None, None, None],
           [None, None, dead, None, None, None, None, None, None],
           [None, dead, None, None, None, None, None, None, None],
           [dead, None, None, None, None, None, None, None, None]]]

game_of_life = Game(base, matrix)

if __name__ == "__main__":

    print(game_of_life.image(alive, [2,6]))
