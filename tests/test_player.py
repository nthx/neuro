# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_player_defaults(self):
        player = HumanPlayer('Tomcio', OUTPOST)
        
        self.assertEquals(Army.MAX_PAWNS, len(player.pawns_deck))
        self.assertEquals(0, len(player.pawns_board))
        self.assertEquals(0, len(player.pawns_thrown))
        self.assertEquals(0, len(player.pawns_hand))
        
        self.assertTrue(player.army is OUTPOST)
        self.assertTrue(player.pawns_deck is not player.army.pawns)
        
        
    def test_01_player_can_take_up_to_3_pawns(self):
        player = HumanPlayer('Tomcio', OUTPOST)
        hq = player.take_hq_from_deck()
        
        self.assertTrue(hq)
        self.assertEquals(Army.MAX_PAWNS-1, len(player.pawns_deck))
        self.assertEquals(0, len(player.pawns_board))
        self.assertEquals(0, len(player.pawns_thrown))
        self.assertEquals(1, len(player.pawns_hand))
        
        
        random1 = player.take_random_pawn()
        self.assertTrue(random1)
        self.assertEquals(Army.MAX_PAWNS-2, len(player.pawns_deck))
        self.assertEquals(0, len(player.pawns_board))
        self.assertEquals(0, len(player.pawns_thrown))
        self.assertEquals(2, len(player.pawns_hand))

        
        random2 = player.take_random_pawn()
        self.assertTrue(random2)
        self.assertEquals(Army.MAX_PAWNS-3, len(player.pawns_deck))
        self.assertEquals(0, len(player.pawns_board))
        self.assertEquals(0, len(player.pawns_thrown))
        self.assertEquals(3, len(player.pawns_hand))

        try:
            random3 = player.take_random_pawn()
            self.fail('Player took 4th pawn in a turn. Not possible')
        except:
            pass
            
        
        
        