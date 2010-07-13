# -*- coding: utf-8 -*-
import logging

import random 

from model.pawn import *
log = logging.getLogger(__name__) #define after '..pawn import *'



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
        if not self.get_hq():
            self.pawns.append(HqPawn(self))
            
        while len(self.pawns) < Army.MAX_PAWNS:   
            self.pawns.append(random.choice([RunnerPawn(self), MedicPawn(self), BattlePawn(self), SniperPawn(self)]))
        
            
    def get_hq(self):
        result = filter(lambda pawn: pawn.am_hq(), self.pawns)
        return result and result[0] or None
        
        
    @classmethod
    def random(cls):
        random.choice(ARMIES)

        

OUTPOST = Army('Posterunek', '#00FF00', hq_color='#00EE00')
MOLOCH = Army('Moloch', 'red')
BORGO = Army('Borgo', '#FFFF00', hq_color='#FFEE00')
HEGEMONIA = Army('Hegemonia', 'blue')
ARMIES = [OUTPOST, MOLOCH, BORGO, HEGEMONIA]
        