# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)


class Pawn(object):
    def __init__(self, army):
        self.army = army
        
        #do not modify defaults
        self.is_immediate = False
        self.can_be_put_on_board = False

    def color(self):
        return self.army.color
    
    def get_name(self):
        return self.__class__.__name__.replace('Pawn', '').lower()
        
    def am_hq(self):
        return False
            
            
class HqPawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True

    def color(self):
        return self.army.hq_color
        
    def get_name(self):
        return 'HQ'

    def am_hq(self):
        return True
    
        
class SoldierAPawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True
        

class SoldierBPawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True
        

class SoldierCPawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True
        

class SniperPawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.is_immediate = True

        
class MoveRotatePawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.is_immediate = True

        
class BattlePawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.is_immediate = True

        
class MedicPawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True
        
        