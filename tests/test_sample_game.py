# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    def test_00_sample_play(self):
        game = Game()
        game.add_player(ComputerPlayer('X-engine', OUTPOST, strategy=RandomStrategy()))
        game.add_player(HumanPlayer('Tomasz', BORGO, strategy=RandomStrategy()))
        
        #game.board.print_graph()
        
        for x in range(5):
            game.player_turn(game.computer())
            #game.board.print_graph()
        
            game.player_turn(game.human())
            #game.board.print_graph()
            
            
        
    