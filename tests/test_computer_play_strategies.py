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
        game.board.print_graph()

        computer = ComputerPlayer('P-Engine', BORGO )
        computer.strategy = PredefinedStrategy(
            predefined_moves=[
                [Move(computer.pawn('hq'), 'A1', 'A')],
                [Move(computer.pawn('runner')[0], 'A2', 'B'), KeepInHand(computer.pawn('battle')[0])],
                [Move(computer.pawn('runner')[1], 'B1', 'C'), Discard(computer.pawn('runner')[2])],
                [Battle(computer.pawn('battle')[0]), Discard(computer.pawn('runner')[3]), Discard(computer.pawn('runner')[4])]
            ]
        )
        game.add_player(computer)
        
        human = HumanPlayer('Tomasz', OUTPOST )
        human.strategy = PredefinedStrategy(
            predefined_moves=[
                [Move(human.pawn('hq'), 'E1', 'F')],
                [Move(human.pawn('runner')[0], 'E2', 'B'), Discard(human.pawn('battle')[0])],
                [Move(human.pawn('runner')[1], 'E3', 'C'), Discard(human.pawn('runner')[2])]
            ]
        )
        game.add_player(human)

        #move c1
        game.player_turn(game.computer())
        game.board.print_graph()
        
        self.assertTrue(game.board.pawn('A1'))
        self.assertEquals('A', game.board.pawn('A1')['direction'])
        self.assertEquals(0, len(computer.pawns_hand))
        self.assertEquals(1, len(computer.pawns_board))
        
        #move h1
        game.player_turn(game.human())
        game.board.print_graph()
        
        self.assertTrue(game.board.pawn('E1'))
        self.assertEquals('F', game.board.pawn('E1')['direction'])
        self.assertEquals(0, len(human.pawns_hand))
        self.assertEquals(1, len(human.pawns_board))

        #move c2
        game.player_turn(game.computer())
        game.board.print_graph()
        
        self.assertTrue(game.board.pawn('A2'))
        self.assertEquals('B', game.board.pawn('A2')['direction'])
        self.assertEquals('runner', game.board.pawn('A2')['pawn'].get_name())
        self.assertEquals(1, len(computer.pawns_hand))
        self.assertEquals(2, len(computer.pawns_board))

        #move h2
        game.player_turn(game.human())
        game.board.print_graph()
        
        self.assertTrue(game.board.pawn('E2'))
        self.assertEquals('B', game.board.pawn('E2')['direction'])
        self.assertEquals('runner', game.board.pawn('E2')['pawn'].get_name())
        self.assertEquals(1, len(human.pawns_discarded))
        self.assertEquals(2, len(computer.pawns_board))

        #move c3
        game.player_turn(game.computer())
        game.board.print_graph()
        
        self.assertEquals('C', game.board.pawn('B1')['direction'])
        self.assertEquals('runner', game.board.pawn('B1')['pawn'].get_name())
        self.assertEquals(1, len(computer.pawns_discarded))
        self.assertEquals(1, len(computer.pawns_hand))
        self.assertEquals(3, len(computer.pawns_board))

        #move h3
        game.player_turn(game.human())
        game.board.print_graph()
        
        self.assertTrue(game.board.pawn('E3'))
        self.assertEquals('C', game.board.pawn('E3')['direction'])
        self.assertEquals('runner', game.board.pawn('E3')['pawn'].get_name())
        self.assertEquals(2, len(human.pawns_discarded))
        self.assertEquals(0, len(human.pawns_hand))
        self.assertEquals(3, len(computer.pawns_board))
                                                                