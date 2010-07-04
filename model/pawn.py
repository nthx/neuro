# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)


class Pawn(object):
    def __init__(self, name, army):
        self.name = name
        self.army = army
        
    def is_base(self):
        return 'base' == self.name
        
    def is_soldier(self):
        return self.name in ['soldier']
        
    def is_module(self):
        return self.name in ['module']
        
    def is_immediate(self):
        return self.name in ['battle', 'move', 'sniper']
        
    def color(self):
        return self.army.color
    