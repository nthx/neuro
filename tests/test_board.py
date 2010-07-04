# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_create_board(self):
        board = Board()
        self.assertEqual(19, len(board.graph.nodes()))
        self.assertEqual(19, len(board.hexes))

        
        for length, space_names in [
                (3, ['A1', 'A3', 'C1', 'C5', 'E1', 'E3']),
                (4, ['A2', 'E2', 'B1', 'B4', 'D1', 'D4']),
                (6, ['B2', 'B3', 'C2', 'C3', 'C4', 'D2', 'D3'])
                           ]:
            for space_name in space_names:
                log.debug(space_name)
                log.debug(board.graph.neighbors(board.hex(space_name)))
                self.assertEqual(length, len(board.graph.neighbors(board.hex(space_name))))

        
        self.assertEqual(42, board.graph.number_of_edges())

        
        
    def test_01_players(self):
        board = Board()
        self.assertEqual(2, len(board.players))
        self.assertTrue(board.players[0].is_computer())
        self.assertTrue(board.players[1].is_human())
        
        self.assertTrue(board.players[0].is_computer() or board.players[1].is_computer())
        self.assertTrue(board.players[0].is_human() or board.players[1].is_human())
        
        computer = board.computer()
        human = board.human()
        self.assertNotEqual(human, computer)
        
        
        self.assertEquals(Army.MAX_PAWNS, len(computer.pawns_deck))
        self.assertEquals(0, len(computer.pawns_board))
        self.assertEquals(0, len(computer.pawns_thrown))
        self.assertEquals(0, len(computer.pawns_hand))
        
        
    def test_02_army(self):
        board = Board()
        human = board.human()
        computer = board.computer()
        self.assertTrue(human.army)
        self.assertEqual(Army.MAX_PAWNS, len(human.army.pawns))
        self.assertEqual(Army.MAX_PAWNS, len(computer.army.pawns))
        self.assertNotEqual(human.army, computer.army)
        
        self.assertTrue(human.army.p_hq())
        self.assertTrue(computer.army.p_hq())

        
    def test_05_moves(self):
        board = Board()
        board.player_turn(board.computer())
        
        self.assertEqual(1, len(board.moves))
        self.assertEqual(1, len(board.pawns()))
        
        
        