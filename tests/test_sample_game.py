# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    def test_00_sample_play(self):
        board = Board()
        board.print_graph()
        
        for x in range(5):
            board.player_turn(board.computer())
            board.print_graph()
        
            board.player_turn(board.human())
            board.print_graph()
        
    