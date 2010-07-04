# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import random

from model.army import Army
from model.move import Move


class Player(object):
    def __init__(self, name, army=None, board=None):
        self.name = name
        self.board = board
        
        if not army:
            army = Army.random()
        self.army = army

        self.pawns_deck = self.army.pawns[:]
        self.pawns_board = []  #pawns put on a board
        self.pawns_thrown = []   #pawns thrown away. Wont be used at all
        self.pawns_hand = []   #pawns kept in a hand for later turn
        
        
    def pick_pawns(self):
        log.debug('%s: pick_pawns', self.name)
        picked = []
        if 0 == len(self.pawns_deck):
            pass
            
        elif (Army.MAX_PAWNS - 0) == len(self.pawns_deck):
            picked.append(self.take_pawn_from_deck(self.take_base_from_deck()))
        
        elif (Army.MAX_PAWNS - 1) == len(self.pawns_deck):
            picked.append(self.take_pawn_from_deck(random.choice(self.pawns_deck)))
            
        elif (Army.MAX_PAWNS - 2) == len(self.pawns_deck):
            picked.append(self.take_pawn_from_deck(random.choice(self.pawns_deck)))
            picked.append(self.take_pawn_from_deck(random.choice(self.pawns_deck)))
            
        else:
            picked.append(self.take_pawn_from_deck(random.choice(self.pawns_deck)))
            picked.append(self.take_pawn_from_deck(random.choice(self.pawns_deck)))
            picked.append(self.take_pawn_from_deck(random.choice(self.pawns_deck)))
            
        picked = [pawn for pawn in picked if pawn is not None]
        log.debug(picked)
        return picked
            
            
    def take_pawn_from_deck(self, pawn):
        if len(self.pawns_hand) >= 3:
            raise Exception('CantHaveMoreThan3OInHand')
        
        self.pawns_deck.remove(pawn)
        self.pawns_hand.append(pawn)
        return pawn
        
        
    def take_base_from_deck(self):
        result = filter(lambda pawn: pawn.is_base(), self.pawns_deck)
        return result and result[0] or None
        
        
    def my_turn(self):
        pawns = self.pick_pawns()
        if len(pawns) > 2:
            to_throw_away = random.choice(pawns)
            pawns.remove(to_throw_away)
            self.pawns_hand.remove(to_throw_away)
            
        for pawn in pawns:
            yield Move(pawn)
        

    def move_made(self, move):
        self.pawns_hand.remove(move.pawn)
        self.pawns_board.append(move.pawn)
        

    def is_human(self):
        pass
        
    def is_computer(self):
        pass
        
        

        
        
class HumanPlayer(Player):
    def is_human(self):
        return True
        
    def is_computer(self):
        return False
    

class ComputerPlayer(Player):
    def is_human(self):
        return False
        
    def is_computer(self):
        return True
        
    