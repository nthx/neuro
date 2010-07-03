# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_create_board(self):
        b = Board()
        self.assertEqual(10, len(board.nodes))

        
