#!/usr/bin/env python
# coding: utf-8

from Configuration import *


class GameOfLife:
    """Defines the rules."""


    def NextState(self, cell,config): 
        if config.isOfState(alive,cell) == True :
            compteur = 0
            for i in range (len(voisin(cell))):
               if config.isOfState(alive,voisin(cell[i])) == True :
                   compteur += 1
            if compteur == 2 or compteur == 3 :
                return alive
            else :
                return dead
        else :
            compteur2 = 0
            for i in range (len(voisin(cell))) :
                if config.isOfState(alive,voisin(cell[i])) == True :
                    compteur2 += 1
            if compteur2 == 3 :
                return alive
            else :
                return dead
                    
        
        return True

    def voisin(self, cell):
        c1=Cell(cell.x + 1, cell.y)
        c2=Cell(cell.x, cell.y + 1)
        c3=Cell(cell.x + 1, cell.y + 1)
        c4=Cell(cell.x - 1, cell.y)
        c5=Cell(cell.x, cell.y - 1)
        c6=Cell(cell.x - 1, cell.y - 1)
        return [c1, c2, c3, c4, c5, c6]
