# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    def test_00_sample_play(self):
        game = Game()
        game.board.print_graph()
        
        for x in range(5):
            game.player_turn(game.computer())
            game.board.print_graph()
        
            game.player_turn(game.human())
            game.board.print_graph()
        
    