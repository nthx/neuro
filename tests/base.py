# -*- coding: utf-8 -*-
import logging

import unittest
import sys

from model.army import Army, POSTERUNEK, BORGO, HEGEMONIA, MOLOCH
from model.board import Board
from model.game import Game
from model.pawn import *


log = logging.getLogger(__name__) #define after '..pawn import *'


class BaseTest(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass

