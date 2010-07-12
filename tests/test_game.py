# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_01_players(self):
        game = Game()
        self.assertEquals(0, len(game.players))
        self.assertEquals(0, len(game.moves))
        
        game.add_player(ComputerPlayer('X-engine', OUTPOST, strategy=RandomStrategy()))
        game.add_player(HumanPlayer('Tomasz', BORGO))
        self.assertEqual(2, len(game.players))
        
        self.assertTrue(game.players[0].is_computer())
        self.assertTrue(game.players[1].is_human())
        
        self.assertTrue(game.players[0].is_computer() or game.players[1].is_computer())
        self.assertTrue(game.players[0].is_human() or game.players[1].is_human())
        
        computer = game.computer()
        human = game.human()
        self.assertNotEqual(human, computer)
        


        
    def test_05_game_with_1_turns(self):
        game = Game()
        game.add_player( ComputerPlayer('X-engine', OUTPOST, strategy=RandomStrategy()))
        game.add_player(HumanPlayer('Tomasz', OUTPOST))

        human = game.human()
        computer = game.computer()

        game.player_turn(computer)
        self.assertEqual(1, len(game.moves))
        self.assertEqual(1, len(game.board.pawns()))
        
        self.assertEquals(Army.MAX_PAWNS-1, len(computer.pawns_deck))
        self.assertEquals(1, len(computer.pawns_board))
        self.assertEquals(0, len(computer.pawns_discarded))
        self.assertEquals(0, len(computer.pawns_hand))
        
        self.assertEquals(Army.MAX_PAWNS, len(human.pawns_deck))
        self.assertEquals(0, len(human.pawns_board))
        
        game.player_turn(human)
        self.assertEqual(2, len(game.moves))
        self.assertEqual(2, len(game.board.pawns()))
        
        self.assertEquals(Army.MAX_PAWNS-1, len(computer.pawns_deck))
        self.assertEquals(1, len(computer.pawns_board))
        self.assertEquals(0, len(computer.pawns_discarded))
        self.assertEquals(0, len(computer.pawns_hand))
        
        self.assertEquals(Army.MAX_PAWNS-1, len(human.pawns_deck))
        self.assertEquals(1, len(human.pawns_board))

        self.assertEquals(0, len(human.pawns_discarded))
        self.assertEquals(0, len(human.pawns_hand))
        