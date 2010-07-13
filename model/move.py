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
        
        self.can_be_done_after_battle_is_played = False

        
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

    def put_yourself_to_board(self, player, board):
        pass       
            
    def __repr__(self):
        return model_repr(self, attrs=['pawn', 'where', 'direction'])

        
        
class Move(BaseMove):
    def __init__(self, pawn=None, where=None, direction=None):
        BaseMove.__init__(self, pawn, where=where, direction=direction)
        self.can_be_done_after_battle_is_played = False

        
    def update_player_pawns(self, player):    
        player.pawns_board.append(self.pawn)
        
        
    def put_yourself_to_board(self, player, board):
        hex = board.hex(self.where)
        hex.put(self.pawn, self.direction)
        
        
class KeepInHand(BaseMove):
    def __init__(self, pawn=None, where=None, direction=None):
        BaseMove.__init__(self, pawn, where=where, direction=direction)
        self.can_be_done_after_battle_is_played = True

        
    def update_player_pawns(self, player):    
        player.pawns_hand.append(self.pawn)

        
        
class Discard(BaseMove):
    def __init__(self, pawn=None, where=None, direction=None):
        BaseMove.__init__(self, pawn, where=where, direction=direction)
        self.can_be_done_after_battle_is_played = True

        
    def update_player_pawns(self, player):    
        player.pawns_discarded.append(self.pawn)
        

        
class Battle(BaseMove):
    def __init__(self, pawn=None, where=None, direction=None):
        BaseMove.__init__(self, pawn, where=where, direction=direction)
        self.can_be_done_after_battle_is_played = False

        
    def update_player_pawns(self, player):
        #after it's used, a game will discard it to player's discarded
        player.pawns_board.append(self.pawn)


    def put_yourself_to_board(self, player, board):
        hex = board.hex_with_player_hq(player)
        hex.put(self.pawn)
    