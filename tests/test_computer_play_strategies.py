# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_different_strategies_available(self):
        game = Game()

        game.add_player( HumanPlayer('Monika', OUTPOST, strategy=RandomStrategy()))

        human = HumanPlayer('Tomasz', OUTPOST)
        human.strategy = PredefinedStrategy(
            predefined_moves=[
                [Move(human.pawn('hq'), 'E1', 'E')]
            ]
        )
        game.add_player(human)

        game.add_player( ComputerPlayer('R-Engine', OUTPOST, strategy=RandomStrategy()))
        
        computer = ComputerPlayer('P-Engine',OUTPOST)
        computer.strategy = PredefinedStrategy(
            predefined_moves=[
                [Move(human.pawn('hq'), 'A1', 'A')]
            ]
        )
        game.add_player(computer)
        
        self.assertEqual(4, len(game.players))
        
        
    def test_01_predefind_game(self):
        game = Game()

        computer = ComputerPlayer('P-Engine', OUTPOST )
        computer.strategy = PredefinedStrategy(
            predefined_moves=[
                [Move(computer.pawn('hq'), 'A1', 'A')],
                [Move(computer.pawn('runner'), 'A2', 'B'), KeepInHand(computer.pawn('battle'))],
                [Move(computer.pawn('runner'), 'B1', 'C'), Discard(computer.pawn('runner'))],
                [Battle(computer.pawn('battle')), Discard(computer.pawn('runner')), Discard(computer.pawn('runner'))]
            ]
        )
        game.add_player(computer)
        
        human = HumanPlayer('Tomasz', OUTPOST )
        human.strategy = strategy=PredefinedStrategy(
            predefined_moves=[
                [Move(human.pawn('hq'), 'E1', 'F')],
                [Move(human.pawn('runner'), 'E2', 'B'), Discard(human.pawn('battle'))],
                [Move(human.pawn('runner'), 'E3', 'C'), Discard(human.pawn('runner'))]
            ]
        )
        game.add_player(human)

        game.player_turn(game.computer())
        
        self.assertTrue(game.board.pawn('A1'))
        self.assertEquals('A', game.board.pawn('A1')['direction'])