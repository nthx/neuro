# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import random 

from model.pawn import Pawn



class Army(object):
    MAX_PAWNS = 35
    
    def __init__(self, name, color, pawns=[]):
        self.name = name
        self.color = color
        self.pawns = pawns[:]
        self.create_random_army()
        
        
    def create_random_army(self):
        if not self.p_base():
            self.pawns.append(Pawn('base', self))
            
        while len(self.pawns) < Army.MAX_PAWNS:   
            self.pawns.append(random.choice([Pawn('soldier', self), Pawn('battle', self)]))
        
            
    def p_base(self):
        result = filter(lambda pawn: pawn.is_base(), self.pawns)
        return result and result[0] or None
        
        
    def p_soldier(self):
        result = filter(lambda pawn: pawn.is_soldier(), self.pawns)
        return result and random.choice(result) or None

        
    @classmethod
    def random(cls):
        random.choice(ARMIES)

        

POSTERUNEK = Army('Posterunek', 'green')
MOLOCH = Army('Moloch', 'red')
BORGO = Army('Borgo', 'yellow')
HEGEMONIA = Army('Hegemonia', 'blue')
ARMIES = [POSTERUNEK, MOLOCH, BORGO, HEGEMONIA]
        