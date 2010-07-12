# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import random
from model.army import Army
from model.move import Move


class Strategy(object):
    
    def __init__(self):
        pass
        
    def moves_by_strategy(self, player):
        raise NotImplemented()
    

class RandomStrategy(Strategy):
    
    def moves_by_strategy(self, player):
        picked = []
        if (Army.MAX_PAWNS - 0) == len(player.pawns_deck):
            hq =player.take_hq_from_deck()
            picked.append(hq)
        
        elif (Army.MAX_PAWNS - 1) == len(player.pawns_deck):
            picked.append(player.take_random_pawn())
            
        elif (Army.MAX_PAWNS - 2) == len(player.pawns_deck):
            picked.append(player.take_random_pawn())
            picked.append(player.take_random_pawn())
            
        else:
            picked.append(player.take_random_pawn())
            picked.append(player.take_random_pawn())
            picked.append(player.take_random_pawn())
            
        for pawn in picked:
            yield Move(pawn,
                       where=player.board.any_empty_hex(), 
                       direction=Move.random_direction())
            
        
    
    
    
class PredefinedStrategy(Strategy):
    
    def __init__(self, predefined_moves):
        Strategy.__init__(self)
        self.predefined_moves = predefined_moves
        pass
