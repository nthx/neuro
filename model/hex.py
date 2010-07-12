# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import random
from util.text import model_repr



class Hex(object):
    
    def __init__(self, position):
        self.position = position
        self.pawn_directions = [] #(pawn, direction) that lie on the hex. 1st = bottom
    
        
    def put(self, pawn, direction):
        self.pawn_directions.append({'pawn':pawn, 'direction':direction})
        
        
    def color(self):
        if self.is_empty():
            return 'white'
        else:
            return self.pawn_directions[0]['pawn'].color()
        
            
    def is_empty(self):
        return len(self.pawn_directions) == 0
        
        
    def __repr__(self):
        if self.pawn_directions:
            return '%(pawn)s\n%(direction)s' % {
                'army': self.pawn_directions[0]['pawn'].army.name,
                'pawn': self.pawn_directions[0]['pawn'].get_repr(),
                'direction': self.pawn_directions[0]['direction']
            }
        else:
            return ''
        
        
                    
