# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)
import random

from util.text import model_repr


class BaseMove(object):
    def __init__(self, pawn=None, where=None, direction=None):
        self.pawn = pawn
        self.where = where
        self.direction = direction

        
    @classmethod
    def random_direction(cls):
        return random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
        
        
    @classmethod
    def object_by_clazz(cls, clazz):
        if 'move' == clazz:
            return Move()
        elif 'discard' == clazz:
            return Discard()
        elif 'keep' == clazz:
            return KeepInHand()
        elif 'battle' == clazz:
            return Battle()

    def put_yourself_to_board(self, board):
        pass       
            
    def __repr__(self):
        return model_repr(self, attrs=['pawn', 'where', 'direction'])

        
        
class Move(BaseMove):
        
    def update_player_pawns(self, player):    
        player.pawns_board.append(self.pawn)
        
        
    def put_yourself_to_board(self, board):
        hex = board.hex(self.where)
        hex.put(self.pawn, self.direction)
        
        
class KeepInHand(BaseMove):
        
    def update_player_pawns(self, player):    
        player.pawns_hand.append(self.pawn)

        
        
class Discard(BaseMove):
        
    def update_player_pawns(self, player):    
        player.pawns_discarded.append(self.pawn)
        

        
class Battle(BaseMove):
    pass
    