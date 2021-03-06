# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import random

from util.text import model_repr

from model.army import Army
from model.strategy import RandomStrategy, PredefinedStrategy



class Player(object):
    def __init__(self, name, army, strategy=None, board=None):
        self.name = name
        self.board = board
        self.strategy = strategy
        
        self.army = army

        self.pawns_deck = self.army.pawns[:]
        self.pawns_board = []  #pawns put on a board
        self.pawns_discarded = []   #pawns thrown away. Wont be used at all
        self.pawns_hand = []   #pawns kept in a hand for later turn
        
        for pawn in army.pawns:
            pawn.player = self
        
        
    def take_pawn_from_deck(self, pawn):
        if len(self.pawns_hand) >= 3:
            raise Exception('CantHaveMoreThan3OInHand')
        
        self.pawns_deck.remove(pawn)
        return pawn
        
        
    def pawn(self, name):
        pawns = filter(lambda pawn: pawn.get_name() == name, self.pawns_deck)
        
        if len(pawns) == 0:
            return None;
            
        elif len(pawns) == 1:
            return pawns[0]
            
        else:
            return pawns
        
        
    def take_hq_from_deck(self):
        result = filter(lambda pawn: pawn.am_hq(), self.pawns_deck)
        if not result or len(result)>1:
            raise HqMustBeNowOnPlayersDeck(result)
        
        return self.take_pawn_from_deck(result[0])
        
        
    def take_random_pawn(self):
        return self.take_pawn_from_deck(random.choice(self.pawns_deck))
        
        
    def my_turn(self):
        if 0 == len(self.pawns_deck):
            raise GameShouldHandleThatSituation()
            
        return self.strategy.moves_by_strategy(self)
        
            
    def is_human(self):
        return False
        
        
    def is_computer(self):
        return False
        
        
    def __repr__(self):
        return model_repr(self, attrs=['name'])

        
        
class HumanPlayer(Player):
    def __init__(self, name, army, strategy=RandomStrategy(), board=None):
        Player.__init__(self, name, army, strategy=strategy, board=board)
        if not strategy:
            raise ComputerMustHaveStrategy()


    def is_human(self):
        return True

        
        
class ComputerPlayer(Player):
    def __init__(self, name, army, strategy=None, board=None):
        Player.__init__(self, name, army, strategy=strategy, board=board)
    
        
    def is_computer(self):
        return True
    
