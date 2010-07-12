# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_army(self):
        army = OUTPOST
        
        self.assertTrue(army)
        self.assertEqual(Army.MAX_PAWNS, len(army.pawns))
        self.assertTrue(army.get_hq())
        
        
        