# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_01_players(self):
        game = Game()
        self.assertEqual(2, len(game.players))
        self.assertTrue(game.players[0].is_computer())
        self.assertTrue(game.players[1].is_human())
        
        self.assertTrue(game.players[0].is_computer() or game.players[1].is_computer())
        self.assertTrue(game.players[0].is_human() or game.players[1].is_human())
        
        computer = game.computer()
        human = game.human()
        self.assertNotEqual(human, computer)
        
        
        self.assertEquals(Army.MAX_PAWNS, len(computer.pawns_deck))
        self.assertEquals(0, len(computer.pawns_board))
        self.assertEquals(0, len(computer.pawns_thrown))
        self.assertEquals(0, len(computer.pawns_hand))
        
        
    def test_02_army(self):
        game = Game()
        human = game.human()
        computer = game.computer()
        self.assertTrue(human.army)
        self.assertEqual(Army.MAX_PAWNS, len(human.army.pawns))
        self.assertEqual(Army.MAX_PAWNS, len(computer.army.pawns))
        self.assertNotEqual(human.army, computer.army)
        
        self.assertTrue(human.army.get_hq())
        self.assertTrue(computer.army.get_hq())

        
    def test_05_moves(self):
        game = Game()
        human = game.human()
        computer = game.computer()

        game.player_turn(computer)
        self.assertEqual(1, len(game.moves))
        self.assertEqual(1, len(game.board.pawns()))
        
        self.assertEquals(Army.MAX_PAWNS-1, len(computer.pawns_deck))
        self.assertEquals(1, len(computer.pawns_board))
        self.assertEquals(0, len(computer.pawns_thrown))
        self.assertEquals(0, len(computer.pawns_hand))
        
        self.assertEquals(Army.MAX_PAWNS, len(human.pawns_deck))
        self.assertEquals(0, len(human.pawns_board))
        
        game.player_turn(human)
        self.assertEqual(2, len(game.moves))
        self.assertEqual(2, len(game.board.pawns()))
        
        self.assertEquals(Army.MAX_PAWNS-1, len(computer.pawns_deck))
        self.assertEquals(1, len(computer.pawns_board))
        self.assertEquals(0, len(computer.pawns_thrown))
        self.assertEquals(0, len(computer.pawns_hand))
        
        self.assertEquals(Army.MAX_PAWNS-1, len(human.pawns_deck))
        self.assertEquals(1, len(human.pawns_board))

        self.assertEquals(0, len(human.pawns_thrown))
        self.assertEquals(0, len(human.pawns_hand))
        