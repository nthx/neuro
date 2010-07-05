# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

from datetime import datetime as dt

from model.army import Army, POSTERUNEK, BORGO, HEGEMONIA, MOLOCH
from model.board import Board
from model.player import HumanPlayer, ComputerPlayer



class Game(object):
    
    
    def __init__(self):
        self.when_started = dt.utcnow()
        
        self.players = []
        self.moves = []
        self.initialize_players()

        self.board = Board(self.moves)

    def initialize_players(self):
        self.players.append(ComputerPlayer('Teddy', army=POSTERUNEK, board=self))
        self.players.append(HumanPlayer('Tomasz', army=BORGO, board=self))

        
    def computer(self):
        return [x for x in self.players if x.is_computer()][0]
        
        
    def human(self):
        return [x for x in self.players if x.is_human()][0]
        
        
    def player_turn(self, player):
        moves = player.my_turn()
        
        for move in moves:
            self._do_move(player, move)

            
    def _do_move(self, player, move):
        if move.pawn.can_be_put_on_board:
            available_hex = self.board.any_empty_hex()
            available_hex.put(move.pawn)
        
        elif move.pawn.is_immediate:
            pass
            
        self.moves.append(move)
        player.move_made(move)
        