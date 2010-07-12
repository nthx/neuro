# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import networkx as nx
import random

from model.hex import Hex


class Board(object):
    def __init__(self, moves=[]):
        self.graph = nx.Graph()
        self.hexes = {}
        self.moves = moves #a reference to game's moves
        
        self.initialize_board()
        
    
    def new_hex(self, name):
        hex = Hex(name)
        self.hexes[name] = hex
        return hex
        
        
    def hex(self, name):
        return self.hexes[name]

        
    def pawn(self, position):
        pawns = self.hex(position).pawn_directions
        if len(pawns) == 0:
            return None;
            
        elif len(pawns) == 1:
            return pawns[0]
            
        else:
            return pawns
        
        
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

        
    def any_empty_hex(self):
        return random.choice([hex for hex in self.graph.nodes() if hex.is_empty()])

        
    def pawns(self):
        pawns = []
        for hex in self.hexes.values():
            pawns.extend(x['pawn'] for x in hex.pawn_directions)
        return pawns
        
        
    def print_graph(self):
        import matplotlib.pyplot as plt
        a=0.2
        b=0.4
        c=0.6
        d=0.8
        a = b = c = d = 0
        x = 0.4
        y = 1.2
        
        plt.figure(figsize=(7,7))
      
        nx.draw_networkx(
            self.graph,
            node_shape='h',
            pos={
                self.hex('A1'): (1+2*x, -0),
                self.hex('A2'): (1+4*x, -0-a),
                self.hex('A3'): (1+6*x, -0-b),
                self.hex('B1'): (1+1*x, -1*y),
                self.hex('B2'): (1+3*x, -1*y-a),
                self.hex('B3'): (1+5*x, -1*y-b),
                self.hex('B4'): (1+7*x, -1*y-c),
                self.hex('C1'): (1+0*x, -2*y),
                self.hex('C2'): (1+2*x, -2*y-a),
                self.hex('C3'): (1+4*x, -2*y-b),
                self.hex('C4'): (1+6*x, -2*y-c),
                self.hex('C5'): (1+8*x, -2*y-d),
                self.hex('D1'): (1+1*x, -3*y),
                self.hex('D2'): (1+3*x, -3*y-a),
                self.hex('D3'): (1+5*x, -3*y-b),
                self.hex('D4'): (1+7*x, -3*y-c),
                self.hex('E1'): (1+2*x, -4*y),
                self.hex('E2'): (1+4*x, -4*y-a),
                self.hex('E3'): (1+6*x, -4*y-b),
            }, 
            with_labels=True,
            node_color=[hex.color() for hex in self.graph],
            node_size=5000)

        filename = 'screenshots/board-%s.png' % str(len(self.moves)).rjust(3, '0')
        plt.savefig(filename)

        