# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import networkx as nx



class Board(object):
    def __init__(self):
        self.graph = nx.Graph()
        self.initialize()

    def initialize(self):
        self.graph.add_nodes_from(['A1', 'A2', 'A3'])
        self.graph.add_nodes_from(['B1', 'B2', 'B3', 'B4'])
        self.graph.add_nodes_from(['C1', 'C2', 'C3', 'C4', 'C5'])
        self.graph.add_nodes_from(['D1', 'D2', 'D3', 'D4'])
        self.graph.add_nodes_from(['E1', 'E2', 'E3'])
        
        
