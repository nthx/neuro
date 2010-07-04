# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import random
from util.text import model_repr



class Hex(object):
    def __init__(self, name):
        self.name = name
        self.pawns = [] #pawns that lie on the hex. 1st = botton
        
    def put(self, pawn):
        self.pawns.append(pawn)
        
    def color(self):
        if self.is_empty():
            return 'white'
        else:
            return self.pawns[0].color()
        
    def is_empty(self):
        return len(self.pawns) == 0
        
    def __repr__(self):
        if self.pawns:
            return '%(pawn)s' % {
                'army': self.pawns[0].army.name,
                'pawn': self.pawns[0].get_name()
            }
        else:
            return ''
        #return model_repr(self, attrs=['name'])
        
        
                    
