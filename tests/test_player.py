# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_player_defaults(self):
        player = HumanPlayer('Tomcio', OUTPOST)
        
        self.assertEquals(Army.MAX_PAWNS, len(player.pawns_deck))
        self.assertEquals(0, len(player.pawns_board))
        self.assertEquals(0, len(player.pawns_discarded))
        self.assertEquals(0, len(player.pawns_hand))
        
        self.assertTrue(player.army is OUTPOST)
        self.assertTrue(player.pawns_deck is not player.army.pawns)
        
        
    def test_01_player_can_take_up_to_3_pawns(self):
        pass

        
    def test_02_predefind_strategy_works(self):
        human = HumanPlayer('Tomasz', OUTPOST, 
            strategy = PredefinedStrategy(
                predefined_moves=[
                    ['move-hq-E1-F'],
                    ['move-runner-E2-B', 'discard-battle'],
                    ['move-runner-E3-C', 'discard-runner']
                ]
            )
        )
        
        human.my_turn()
        
        self.assertEquals(0, len(human.pawns_hand))
        self.assertEquals(Army.MAX_PAWNS - 1, len(human.pawns_deck))
        self.assertEquals(0, len(human.pawns_discarded))
        self.assertEquals(1, len(human.pawns_board))
        