#!/usr/bin/env python
# coding: utf-8

from Configuration import *

def juliette(configuration):
    if not isinstance(configuration, Configuration):
        raise Exception("bad arguments")
    return len(configuration.cells)
