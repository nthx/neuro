# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import random 

from model.pawn import Pawn



class Army(object):
    MAX_PAWNS = 35
    
    def __init__(self, name, color, hq_color=None, pawns=[]):
        self.name = name
        self.color = color
        self.pawns = pawns[:]
        self.create_random_army()
        if not hq_color:
            hq_color = color
        self.hq_color = hq_color
        
        
    def create_random_army(self):
        if not self.p_hq():
            self.pawns.append(Pawn('hq', self))
            
        while len(self.pawns) < Army.MAX_PAWNS:   
            self.pawns.append(random.choice([Pawn('soldier', self), Pawn('battle', self)]))
        
            
    def p_hq(self):
        result = filter(lambda pawn: pawn.is_hq(), self.pawns)
        return result and result[0] or None
        
        
    def p_soldier(self):
        result = filter(lambda pawn: pawn.is_soldier(), self.pawns)
        return result and random.choice(result) or None

        
    @classmethod
    def random(cls):
        random.choice(ARMIES)

        

POSTERUNEK = Army('Posterunek', '#00FF00', hq_color='#00EE00')
MOLOCH = Army('Moloch', 'red')
BORGO = Army('Borgo', '#FFFF00', hq_color='#FFEE00')
HEGEMONIA = Army('Hegemonia', 'blue')
ARMIES = [POSTERUNEK, MOLOCH, BORGO, HEGEMONIA]
        