# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

from datetime import datetime as dt

from model.army import Army, OUTPOST, BORGO, HEGEMONIA, MOLOCH
from model.board import Board
from model.player import HumanPlayer, ComputerPlayer



class Game(object):
    
    def __init__(self, print_graph=False):
        self.when_started = dt.utcnow()
        
        self.players = []
        self.turns = [[]] #element = a list of moves
        self.turn = 0
        
        self.print_graph = print_graph

        self.board = Board(self)
        
        if self.print_graph:
            self.board.print_graph()
        
    def moves_all(self):
        moves = []
        for turn in self.turns:
            moves.extend(turn)
        
        return moves

    def append_move(self, move):
        if self.turn > len(self.turns):
            aself.turns.append([])
        self.turns[self.turn].append(move)
        

    def current_turn(self):
        if self.turn >= len(self.turns):
            self.turns.append([])
        return self.turns[self.turn]
        
        
    def add_player(self, player):
        player.board = self.board
        self.players.append(player)

        
    def computer(self):
        return [x for x in self.players if x.is_computer()][0]
        
        
    def human(self):
        return [x for x in self.players if x.is_human()][0]
        
        
    def player_turn(self, player):
        player_moves = player.my_turn()
        
        for move in player_moves:
            self.check_and_play_player_move(player, move)

        if self.battle_conditions_met():
            self.battle()
                
        if self.print_graph:
            self.board.print_graph()

        self.turn += 1

            
    def check_and_play_player_move(self, player, move):
        if self.battle_conditions_met():
            self.validate_move_can_be_played_after_battle_is_played(move)
            
        move.put_yourself_to_board(player, self.board)
        self.append_move(move)
        
        
    def validate_move_can_be_played_after_battle_is_played(self, move):
        if not move.can_be_done_after_battle_is_played:
            raise Exception('Move was made which cant go to a board after battle is used before: %s', move)
        
            
    def rule_move_causes_battle(self, move):
        #TODO: another rule here: if that is move after any player's last move, then also a battle
        if move.__class__.__name__.lower() == 'battle':
            return True
        else:
            return False
            
            
    def battle_conditions_met(self):
        for move in self.current_turn():
            if self.rule_move_causes_battle(move):
                return True
                
        if self.board.rule_is_full_for_battle():
            return True
            
        return False
        

    def battle(self):
        raise Exception('not implemented')
            
            
        
