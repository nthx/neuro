# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)
import random


class Move(object):
    def __init__(self, pawn, where=None, direction=None):
        self.pawn = pawn
        self.where = None
        self.direction = None
        
        
    @classmethod
    def random_direction(cls):
        return random.choice(['A', 'B', 'C', 'D', 'E', 'F'])

        
class KeepInHand(Move):
    def __init__(self, pawn):
        Move.__init__(self, pawn)
      
        
class Discard(Move):
    def __init__(self, pawn):
        Move.__init__(self, pawn)

        
class Battle(Move):
    def __init__(self, pawn):
        Move.__init__(self, pawn)
    
    