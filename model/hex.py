# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import random
from util.text import model_repr



class Hex(object):
    
    def __init__(self, position):
        self.position = position
        self.pawn_directions = [] #(pawn, direction) that lie on the hex. 1st = bottom
    
        
    def put(self, pawn, direction='A'):
        self.pawn_directions.append({'pawn':pawn, 'direction':direction})
      
        
    def clear(self):
        self.pawn_directions = []
        
        
    def has_player_hq(self, player):
        for pawn_direction in self.pawn_directions:
            if pawn_direction['pawn'].player == player and pawn_direction['pawn'].am_hq():
                return True
        return False
      
        
    def paws_count_to_battle(self):
        for pawn_direction in self.pawn_directions:
            #TODO: check mine+runner in last move if it works
            if not pawn_direction['pawn'].counts_to_battle:
                return False
                
        return True
        
        
    def color(self):
        if self.is_empty():
            return 'white'
        else:
            return self.pawn_directions[0]['pawn'].color()
        
            
    def is_empty(self):
        return len(self.pawn_directions) == 0
        
        
    def __repr__(self):
        if self.pawn_directions:
            return '%(army)s\n%(pawn)s%(direction)s' % {
                'army': self.pawn_directions[0]['pawn'].army.name,
                'pawn': self.pawn_directions[0]['pawn'].get_repr(),
                'direction': self.pawn_directions[0]['direction']
            }
        else:
            return ''
