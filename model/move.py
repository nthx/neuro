# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

class Move(object):
    def __init__(self, pawn):
        self.pawn = pawn
        self.direction = None
        self.where = None