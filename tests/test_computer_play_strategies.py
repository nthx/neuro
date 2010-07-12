# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_different_strategies_available(self):
        game = Game()

        
        game.add_player(
            HumanPlayer('Monika', 
                OUTPOST,
                strategy=RandomStrategy()
            )
        )
        
        game.add_player(
            HumanPlayer('Tomasz', 
                OUTPOST,
                strategy=PredefinedStrategy(
                    predefined_moves=[
                        [Move(HqPawn(), 'E1', 'F')],
                        [Move(RunnerPawn(), 'E2', 'B'), Discard(BattlePawn())],
                        [Move(RunnerPawn(), 'E3', 'C'), Discard(RunnerPawn())]
                    ]
                )
            )
        )

        game.add_player(
            ComputerPlayer('R-Engine', 
                OUTPOST, 
                strategy=RandomStrategy())
        )
        game.add_player(
            ComputerPlayer('P-Engine', 
                OUTPOST, 
                strategy=PredefinedStrategy(
                    predefined_moves=[
                        [Move(HqPawn(), 'A1', 'A')],
                        [Move(RunnerPawn(), 'A2', 'B'), KeepInHand(BattlePawn())],
                        [Move(RunnerPawn(), 'B1', 'C'), Discard(RunnerPawn())],
                        [Battle(BattlePawn()), Discard(RunnerPawn()), Discard(RunnerPawn())]
                    ]
                )
            )
        )
        
        

        self.assertEqual(4, len(game.players))
        
    def test_01_predefind_game(self):
        game = Game()

        game.add_player(
            ComputerPlayer('P-Engine', 
                OUTPOST, 
                strategy=PredefinedStrategy(
                    predefined_moves=[
                        [Move(HqPawn(), 'A1', 'A')],
                        [Move(RunnerPawn(), 'A2', 'B'), KeepInHand(BattlePawn())],
                        [Move(RunnerPawn(), 'B1', 'C'), Discard(RunnerPawn())],
                        [Battle(BattlePawn()), Discard(RunnerPawn()), Discard(RunnerPawn())]
                    ]
                )
            )
        )
        
        game.add_player(
            HumanPlayer('Tomasz', 
                OUTPOST,
                strategy=PredefinedStrategy(
                    predefined_moves=[
                        [Move(HqPawn(), 'E1', 'F')],
                        [Move(RunnerPawn(), 'E2', 'B'), Discard(BattlePawn())],
                        [Move(RunnerPawn(), 'E3', 'C'), Discard(RunnerPawn())]
                    ]
                )
            )
        )
        
        game.player_turn(game.computer())
        
#        self.assertTrue(game.board.pawn('A1'))
#        self.assertEquals('A', game.board.pawn('A1').direction)