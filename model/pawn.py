# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)


class Pawn(object):
    def __init__(self, name, army):
        self.name = name
        self.army = army
        
    def is_base(self):
        return 'base' == self.name
        
    def color(self):
        return self.army.color
    