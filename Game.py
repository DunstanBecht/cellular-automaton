#!/usr/bin/env python
# coding: utf-8

from Configuration import *


class Game:
    """Defines the rules."""


    def alive(self, cell): 
        if isOfState(cell) == True :
            compteur = 0
            for i in range (len(voisin(cell))):
               if isOfState(voisin(cell[i])) == True :
                   compteur += 1
            if compteur == 2 or compteur == 3 :
                return True
            else :
                return False
        else :
            compteur2 = 0
            for i in range (len(voisin(cell))) :
                if isOfState(voisin(cell[i])) == True :
                    compteur2 += 1
            if compteur2 == 3 :
                return True
            else :
                return False
                    
        
        return True

    def voisin(self, cell):
        return []

class GameOfLife(Game):

    def alive(self, configuration,  cell): 
        # self.voisin(cell) ->liste de cellules
        # 
        return True

    def voisin(self, cell):
        return []