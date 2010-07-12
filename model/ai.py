# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import random
from model.army import Army
from model.move import Move, Discard


class Strategy(object):
    
    def __init__(self):
        pass
        
    def moves_by_strategy(self, player):
        raise NotImplemented()
    

class RandomStrategy(Strategy):
    
    def moves_by_strategy(self, player):
        picked = []
        if (Army.MAX_PAWNS - 0) == len(player.pawns_deck):
            picked.append(player.take_hq_from_deck())
        
        elif (Army.MAX_PAWNS - 1) == len(player.pawns_deck):
            picked.append(player.take_random_pawn())
            
        elif (Army.MAX_PAWNS - 2) == len(player.pawns_deck):
            picked.append(player.take_random_pawn())
            picked.append(player.take_random_pawn())
            
        else:
            picked.append(player.take_random_pawn())
            picked.append(player.take_random_pawn())
            picked.append(player.take_random_pawn())
            
        moves = []
        for i, pawn in enumerate(picked):
            if i in [0, 1]:
                move = Move(pawn,
                    where=player.board.any_empty_hex().position,
                    direction=Move.random_direction()
                )
                
            else:
                move = Discard(pawn)

            move.update_player_pawns(player)
            
            moves.append(move)
        
        return moves
    
    
    
class PredefinedStrategy(Strategy):
    
    def __init__(self, predefined_moves):
        Strategy.__init__(self)
        self.predefined_moves = predefined_moves

        
    def current_turn(self):
        return self.predefined_moves.pop(0)
        
        
    def moves_by_strategy(self, player):
        turn = self.current_turn()
        moves = []
        for move in turn:
            log.debug(player.name)
            log.debug(move)
            player.take_pawn_from_deck(move.pawn)
            move.update_player_pawns(player)
            moves.append(move)
        
        return moves
        