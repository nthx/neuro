# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import random

from model.ai import RandomStrategy, PredefinedStrategy
from model.army import Army
from model.move import Move
from model.ui import UIConsoleStrategy

class Player(object):
    
    def __init__(self, name, army, strategy=None, board=None):
        self.name = name
        self.board = board
        self.strategy = strategy
        
        if not army:
            army = Army.random()
        self.army = army

        self.pawns_deck = self.army.pawns[:]
        self.pawns_board = []  #pawns put on a board
        self.pawns_thrown = []   #pawns thrown away. Wont be used at all
        self.pawns_hand = []   #pawns kept in a hand for later turn
        
        
    def take_pawn_from_deck(self, pawn):
        if len(self.pawns_hand) >= 3:
            raise Exception('CantHaveMoreThan3OInHand')
        
        self.pawns_deck.remove(pawn)
        self.pawns_hand.append(pawn)
        return pawn
        
        
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
        
        moves = self.my_moves()
            
        return moves
        

    def my_moves(self):
        log.debug('%s: my_moves', self.name)
        return self.strategy.moves_by_strategy(self)
            
            
    def move_made(self, move):
        self.pawns_hand.remove(move.pawn)
        self.pawns_board.append(move.pawn)
        

    def is_human(self):
        raise OverrideMethod('is_human')
        
        
    def is_computer(self):
        raise OverrideMethod('is_computer')
        
        

        
        
class HumanPlayer(Player):
    
    def __init__(self, name, army, strategy=RandomStrategy(), board=None):
        Player.__init__(self, name, army, strategy=strategy, board=board)
        if not strategy:
            raise ComputerMustHaveStrategy()


    def is_human(self):
        return True
        
        
    def is_computer(self):
        return False


        
class ComputerPlayer(Player):

    def __init__(self, name, army, strategy=None, board=None):
        Player.__init__(self, name, army, strategy=strategy, board=board)
        if not strategy:
            raise ComputerMustHaveStrategy()
            
    
    def is_human(self):
        return False
    
        
    def is_computer(self):
        return True
        
    