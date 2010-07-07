# -*- coding: utf-8 -*-
import logging

from model.action import *
log = logging.getLogger(__name__) #define after '..pawn import *'



class Pawn(object):
    def __init__(self, army):
        self.army = army
        
        #do not modify defaults
        self.is_immediate = False
        self.can_be_put_on_board = False
        self.is_mobile = False
        
        self.actions = {}
        self.initiative = None
        self.extra_armor = None

    def color(self):
        return self.army.color
    
    def get_name(self):
        initiative = 'X'
        armor = ''
        actions = ''

        if None == self.initiative:
            initiative = '(X)'
        else:
            initiative = '(%s)' % self.initiative

        if None == self.extra_armor:
            armor = ''
        else:
            armor = '+%s' % self.extra_armor
            
        for direction in sorted(self.actions):
            actions += '%s: ' % direction
            for action in self.actions[direction]:
                actions += action.text_repr()
            actions += '\n'
            
        
        return \
            "%(name)s\n%(initiative)s %(armor)s\n%(actions)s" % {
                'name': self.__class__.__name__.replace('Pawn', '').lower(),
                'initiative': initiative,
                'armor': armor,
                'actions': actions
            }
        
    def am_hq(self):
        return False
        
    def action(self, direction, name):
        for action in self.actions.get(direction, []):
            if name == action.name():
                return action
        return NullAction()
        
            
class HqPawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True
        self.initiative = [0]
        self.actions = {
            'A': [Melee(1)],
            'B': [Melee(1)],
            'C': [Melee(1)],
            'D': [Melee(1)],
            'E': [Melee(1)],
            'F': [Melee(1)]
        }

    def color(self):
        return self.army.hq_color
        
    def am_hq(self):
        return True
    
        
class SoldierAPawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True
        self.initiative = [3]
        self.actions = {
            'B': [Range(1)],
        }
        

class SoldierBPawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True
        self.initiative = [3]
        self.actions = {
            'B': [Range(2)],
        }
        

class SoldierCPawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True
        self.initiative = [1]
        self.actions = {
            'A': [Range(1), WhiteArmor()],
            'B': [Melee(1), WhiteArmor()],
            'F': [WhiteArmor()],
        }
        self.extra_armor = 1
        

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
        self.actions = {
            'A': [Heal()],
            'C': [Heal()],
            'E': [Heal()],
        }
        

class Runner(Pawn):
    def __init__(self, army=None):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True
        self.actions = {
            'A': [Melee(1)]
        }
        self.initiative = [2]
        self.is_mobile = True
