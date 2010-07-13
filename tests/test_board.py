# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_create_board(self):
        board = Board()
        self.assertEqual(19, len(board.graph.nodes()))
        self.assertEqual(19, len(board.hexes))
        self.assertEqual(0, len(board.pawns()))
        self.assertFalse(board.rule_is_full_for_battle())
        
        for length, positions in [
            (3, ['A1', 'A3', 'C1', 'C5', 'E1', 'E3']),
            (4, ['A2', 'E2', 'B1', 'B4', 'D1', 'D4']),
            (6, ['B2', 'B3', 'C2', 'C3', 'C4', 'D2', 'D3'])]:
            for position in positions:
                self.assertEqual(length, len(board.graph.neighbors(board.hex(position))))

        self.assertEqual(42, board.graph.number_of_edges())
        

    def test_01_rule_is_full_for_battle(self):
        board = Board()
        for hex in board.hexes.values():
            hex.put(RunnerPawn())
            
        self.assertEqual(19, len(board.pawns()))
        self.assertTrue(board.rule_is_full_for_battle())
        
        
        board = Board()
        for hex in board.hexes.values():
            hex.put(RunnerPawn())
        hex.clear()
            
        self.assertEqual(18, len(board.pawns()))
        self.assertFalse(board.rule_is_full_for_battle())
        
        
        