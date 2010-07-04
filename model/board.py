# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import networkx as nx
import random

from model.army import Army, POSTERUNEK, BORGO, HEGEMONIA, MOLOCH
from model.hex import Hex
from model.player import HumanPlayer, ComputerPlayer


class Board(object):
    def __init__(self):
        self.graph = nx.Graph()
        self.hexes = {}
        self.moves = []
        self.players = []
        
        self.initialize_board()
        self.initialize_players()
        
    
    def new_hex(self, name):
        hex = Hex(name)
        self.hexes[name] = hex
        return hex
        
        
    def hex(self, name):
        return self.hexes[name]

        
    def connect(self, node_pairs):
        for node_pair in node_pairs:
            #log.debug('connect: %s-%s', self.hex(node_pair[0]), self.hex(node_pair[1]))
            self.graph.add_edge(self.hex(node_pair[0]), self.hex(node_pair[1]))
        
        
    def initialize_board(self):
        for name in ['A1', 'A2', 'A3', 
                           'B1', 'B2', 'B3', 'B4',
                           'C1', 'C2', 'C3', 'C4', 'C5',
                           'D1', 'D2', 'D3', 'D4',
                           'E1', 'E2', 'E3']:
            self.graph.add_node(self.new_hex(name))
        
        self.connect([('A1', 'A2'), ('A1', 'B1'), ('A1', 'B2')])
        self.connect([('A2', 'A3'), ('A2', 'B2'), ('A2', 'B3')])
        self.connect([('A3', 'B3'), ('A3', 'B4')])
        
        self.connect([('B1', 'B2'), ('B1', 'C1'), ('B1', 'C2')])
        self.connect([('B2', 'B3'), ('B2', 'C2'), ('B2', 'C3')])
        self.connect([('B3', 'B4'), ('B3', 'C3'), ('B3', 'C4')])
        self.connect([('B4', 'C4'), ('B4', 'C5')])
        
        self.connect([('C1', 'C2'), ('C1', 'D1')])
        self.connect([('C2', 'C3'), ('C2', 'D1'), ('C2', 'D2')])
        self.connect([('C3', 'C4'), ('C3', 'D2'), ('C3', 'D3')])
        self.connect([('C4', 'C5'), ('C4', 'D3'), ('C4', 'D4')])
        self.connect([('C5', 'D4')])

        self.connect([('D1', 'D2'), ('D1', 'E1')])
        self.connect([('D2', 'D3'), ('D2', 'E1'), ('D2', 'E2')])
        self.connect([('D3', 'D4'), ('D3', 'E2'), ('D3', 'E3')])
        self.connect([('D4', 'E3')])

        self.connect([('E1', 'E2')])
        self.connect([('E2', 'E3')])

        
    def initialize_players(self):
        self.players.append(ComputerPlayer('Teddy', army=POSTERUNEK, board=self))
        self.players.append(HumanPlayer('Tomasz', army=BORGO, board=self))

        
    def computer(self):
        return [x for x in self.players if x.is_computer()][0]
        
        
    def human(self):
        return [x for x in self.players if x.is_human()][0]
        
        
    def make_move(self, player):
        moves = player.make_move()
        
        for move in moves:
            self._do_move(player, move)

            
    def _do_move(self, player, move):
        #TODO: fake impl
        available_hex = self.any_empty_hex()
        available_hex.put(move.pawn)
        self.moves.append(move)
        player.move_made(move)
        
    def any_empty_hex(self):
        return random.choice([hex for hex in self.graph.nodes() if hex.is_empty()])
        
    def pawns(self):
        pawns = []
        for hex in self.hexes.values():
            pawns.extend(hex.pawns)
        return pawns
        
        
    def print_graph(self):
        import matplotlib.pyplot as plt
        nx.draw(
            self.graph, 
            pos={
                self.hex('A1'): (3, -0),
                self.hex('A2'): (5, -0.2),
                self.hex('A3'): (7, -0.4),
                self.hex('B1'): (2, -1),
                self.hex('B2'): (4, -1.2),
                self.hex('B3'): (6, -1.4),
                self.hex('B4'): (8, -1.6),
                self.hex('C1'): (1, -2),
                self.hex('C2'): (3, -2.2),
                self.hex('C3'): (5, -2.4),
                self.hex('C4'): (7, -2.6),
                self.hex('C5'): (9, -2.8),
                self.hex('D1'): (2, -3),
                self.hex('D2'): (4, -3.2),
                self.hex('D3'): (6, -3.4),
                self.hex('D4'): (8, -3.6),
                self.hex('E1'): (3, -4),
                self.hex('E2'): (5, -4.2),
                self.hex('E3'): (7, -4.4),
            }, 
            with_labels=True,
            node_color=[hex.color() for hex in sorted(self.hexes.values(), key=lambda hex: hex.name)])
        #node_size=40,
        #     node_color=c,
        #     vmin=0.0,
        #     vmax=1.0,
        #     with_labels=False
        
        
        filename = 'screenshots/board-%s.png' % str(len(self.moves)).rjust(3, '0')
        plt.savefig(filename)

        