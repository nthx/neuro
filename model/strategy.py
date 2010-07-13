# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import random
from model.army import Army
from model.move import BaseMove, Move, Discard


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
        self.parsed = False

        
    def current_turn(self, player):
        if not self.parsed:
            self.parse_text_moves(player)
        return self.predefined_moves.pop(0)
        
    
    def parse_text_moves(self, player):
        self.parsed = True
        pawns_used = {} #key = text_name, value = how many times used in predefined moves
        def parse(text_move):
            """@in: move-hq-A1-A
            @in: discard-runner
            """
            s = text_move.split('-')
            clazz = s[0]
            pawn_name = s[1]
            where = len(s) > 2 and s[2] or None
            direction = len(s) > 3 and s[3] or None
            if pawn_name not in pawns_used:
                pawns_used[pawn_name] = 0
            
            pawns = filter(lambda pawn: pawn.get_name() == pawn_name, player.pawns_deck)
            pawn = pawns[pawns_used[pawn_name]]
            pawns_used[pawn_name] += 1
            move = BaseMove.object_by_clazz(clazz)
            move.pawn = pawn
            move.where = where
            move.direction = direction
            return move
            
        text_moves = self.predefined_moves
        self.predefined_moves = []
        for turn in text_moves:
            real_moves = []
            for text_move in turn:
                real_moves.append(parse(text_move))
            self.predefined_moves.append(real_moves)
            
        
    def moves_by_strategy(self, player):
        turn = self.current_turn(player)
        moves = []
        for move in turn:
            player.take_pawn_from_deck(move.pawn)
            move.update_player_pawns(player)
            moves.append(move)
        
        return moves
        