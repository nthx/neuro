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
        self.moves = []
        self.print_graph = print_graph

        self.board = Board(self.moves)
        
        if self.print_graph:
            self.board.print_graph()
        

    def add_player(self, player):
        player.board = self.board
        self.players.append(player)

        
    def computer(self):
        return [x for x in self.players if x.is_computer()][0]
        
        
    def human(self):
        return [x for x in self.players if x.is_human()][0]
        
        
    def player_turn(self, player):
        moves = player.my_turn()
        
        for move in moves:
            self._do_move(player, move)
            
        if self.print_graph:
            self.board.print_graph()

            
    def _do_move(self, player, move):
        if move.pawn.can_be_put_on_board:
            move.put_yourself_to_board(self.board)
            
        elif move.pawn.is_immediate:
            pass
            
        self.moves.append(move)
        
