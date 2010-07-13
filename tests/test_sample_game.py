# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    def test_00_sample_play(self):
        game = Game(print_graph=False)
        game.add_player(ComputerPlayer('X-engine', OUTPOST, strategy=RandomStrategy()))
        game.add_player(HumanPlayer('Tomasz', BORGO, strategy=RandomStrategy()))
        
        for x in range(5):
            game.player_turn(game.computer())
        
            game.player_turn(game.human())
        
    