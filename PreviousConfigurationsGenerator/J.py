#!/usr/bin/env python
# coding: utf-8

def juliette(game):
    def aux(configuration):
        Considered = configuration.copy()
        for i in range(len(configuration.cells)):
            for v in game.voisin(configuration.cells[i]):
                if not v in Considered.cells[0] :
                    Considered.cells.append(v)
                    Considered.states.append(configuration.stateOf(v))
        Preced = Considered.copy
        Preced.states = [defaultState for i in range(len(Preced.states))]
        def aux2(c, config, configini, base, considered) :
            if nextConfiguration(config) == configini :
                return config
            else :
                for i in base :
                    c.index = index
                    config.states[index] = i
                    aux(Considered[index + 1], config,configini, base, considered)

        return aux2(Considered.cells[0], Preced, configuration, game.base, Considered.cells)
    return aux
