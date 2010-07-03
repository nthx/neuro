# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_create_board(self):
        board = Board()
        self.assertEqual(19, len(board.graph.nodes()))

        
