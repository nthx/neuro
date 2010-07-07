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

        
        
        