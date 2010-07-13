# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_battle_with_predefined_moves(self):
        game = Game(print_graph=True)

        game.add_player(ComputerPlayer('P-Engine', BORGO, 
            strategy = PredefinedStrategy(
            predefined_moves=[
                ['move-hq-A1-A'],
                ['move-runner-A2-B', 'keep-battle'],
                ['move-sniper-E2-B', 'discard-runner'],
                ['battle-battle', 'discard-runner', 'discard-runner'],
            ]
        )))
        
        game.add_player(HumanPlayer('Tomasz', OUTPOST,
            strategy = PredefinedStrategy(
                predefined_moves=[
                    ['move-hq-E1-F'],
                    ['move-runner-E2-B', 'discard-battle'],
                    ['move-runner-E3-C', 'discard-runner']
                ]
        )))
        computer = game.computer()
        human = game.human()

        game.player_turn(computer)
        game.player_turn(human)
        game.player_turn(computer)
        game.player_turn(human)
        game.player_turn(computer)
        game.player_turn(human)
        
        #next turn should be battle by computer
        try:
            game.player_turn(computer)
            self.fail('should have battle')
        except:
            pass
        finally:
            pass
    