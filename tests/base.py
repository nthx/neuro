# -*- coding: utf-8 -*-
import logging

import unittest
import sys

from model.ai import RandomStrategy, PredefinedStrategy
from model.army import Army, OUTPOST, BORGO, HEGEMONIA, MOLOCH
from model.board import Board
from model.game import Game
from model.move import BaseMove, Move, Discard, Battle, KeepInHand
from model.pawn import *
from model.player import HumanPlayer, ComputerPlayer


log = logging.getLogger(__name__) #define after '..pawn import *'


class BaseTest(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass

