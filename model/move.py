# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)
import random

from util.text import model_repr


class Move(object):
    def __init__(self, pawn, where=None, direction=None):
        self.pawn = pawn
        self.where = where
        self.direction = direction
        
        
    @classmethod
    def random_direction(cls):
        return random.choice(['A', 'B', 'C', 'D', 'E', 'F'])

        
    def update_player_pawns(self, player):    
        player.pawns_board.append(self.pawn)
        
        
    def put_yourself_to_board(self, board):
        hex = board.hex(self.where)
        hex.put(self.pawn, self.direction)
        
        
    def __repr__(self):
        return model_repr(self, attrs=['pawn', 'where', 'direction'])
        
        
class KeepInHand(Move):
    def __init__(self, pawn):
        Move.__init__(self, pawn)

        
    def update_player_pawns(self, player):    
        player.pawns_hand.append(self.pawn)

        
    def put_yourself_to_board(self, board):
        pass        
        
        
class Discard(Move):
    def __init__(self, pawn):
        Move.__init__(self, pawn)

        
    def update_player_pawns(self, player):    
        player.pawns_discarded.append(self.pawn)
        

    def put_yourself_to_board(self, board):
        pass        
        
        
class Battle(Move):
    def __init__(self, pawn):
        Move.__init__(self, pawn)
    

    def put_yourself_to_board(self, board):
        pass    