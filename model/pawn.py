# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)


class Pawn(object):
    def __init__(self, name, army):
        self.name = name
        self.army = army
        
    def is_hq(self):
        return 'hq' == self.name
        
    def is_soldier(self):
        return self.name in ['soldier']
        
    def is_module(self):
        return self.name in ['module']
        
    def is_immediate(self):
        return self.name in ['battle', 'move', 'sniper']
        
    def color(self):
        if self.is_hq():
            return self.army.hq_color
        else:
            return self.army.color
    
    def get_name(self):
        if self.is_hq():
            return 'HQ'
        else:
            return self.name