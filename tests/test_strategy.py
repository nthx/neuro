# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_different_strategies_available(self):
        game = Game()

        game.add_player(HumanPlayer('Monika', OUTPOST, strategy=RandomStrategy()))

        game.add_player(HumanPlayer('Tomasz', OUTPOST,
            strategy = PredefinedStrategy(
            predefined_moves=[
                ['move-hq-E1-E']
            ]
        )))

        game.add_player(ComputerPlayer('R-Engine', OUTPOST, strategy=RandomStrategy()))
        
        game.add_player(ComputerPlayer('P-Engine', OUTPOST,
            strategy = PredefinedStrategy(
                predefined_moves=[
                    ['move-hq-A1-A']
                ]
        )))
        
        self.assertEqual(4, len(game.players))
        
        
    def test_01_predefind_game(self):
        game = Game(print_graph=False)

        game.add_player(ComputerPlayer('P-Engine', BORGO, 
            strategy = PredefinedStrategy(
            predefined_moves=[
                ['move-hq-A1-A'],
                ['move-runner-A2-B', 'keep-battle'],
                ['move-runner-B1-C', 'discard-runner'],
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

        #move c1
        game.player_turn(computer)
        
        self.assertTrue(game.board.pawn('A1'))
        self.assertEquals('A', game.board.pawn('A1')['direction'])
        self.assertEquals(0, len(computer.pawns_hand))
        self.assertEquals(1, len(computer.pawns_board))
        
        #move h1
        game.player_turn(human)
        
        self.assertTrue(game.board.pawn('E1'))
        self.assertEquals('F', game.board.pawn('E1')['direction'])
        self.assertEquals(0, len(human.pawns_hand))
        self.assertEquals(1, len(human.pawns_board))

        #move c2
        game.player_turn(computer)
        
        self.assertTrue(game.board.pawn('A2'))
        self.assertEquals('B', game.board.pawn('A2')['direction'])
        self.assertEquals('runner', game.board.pawn('A2')['pawn'].get_name())
        self.assertEquals(1, len(computer.pawns_hand))
        self.assertEquals(2, len(computer.pawns_board))

        #move h2
        game.player_turn(human)
        
        self.assertTrue(game.board.pawn('E2'))
        self.assertEquals('B', game.board.pawn('E2')['direction'])
        self.assertEquals('runner', game.board.pawn('E2')['pawn'].get_name())
        self.assertEquals(1, len(human.pawns_discarded))
        self.assertEquals(2, len(computer.pawns_board))

        #move c3
        game.player_turn(computer)
        
        self.assertEquals('C', game.board.pawn('B1')['direction'])
        self.assertEquals('runner', game.board.pawn('B1')['pawn'].get_name())
        self.assertEquals(1, len(computer.pawns_discarded))
        self.assertEquals(1, len(computer.pawns_hand))
        self.assertEquals(3, len(computer.pawns_board))

        #move h3
        game.player_turn(human)
        
        self.assertTrue(game.board.pawn('E3'))
        self.assertEquals('C', game.board.pawn('E3')['direction'])
        self.assertEquals('runner', game.board.pawn('E3')['pawn'].get_name())
        self.assertEquals(2, len(human.pawns_discarded))
        self.assertEquals(0, len(human.pawns_hand))
        self.assertEquals(3, len(computer.pawns_board))
                                                                