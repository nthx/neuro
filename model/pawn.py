# -*- coding: utf-8 -*-
import logging

from model.action import *
log = logging.getLogger(__name__) #define after '..pawn import *'

from util.text import model_repr


class Pawn(object):
    def __init__(self, army):
        self.army = army
        
        #do not modify defaults
        self.is_immediate = False
        self.can_be_put_on_board = False
        self.is_mobile = False
        
        self.actions = {}
        self.initiative = []
        self.extra_armor = None

        
    def color(self):
        return self.army.color
    
        
    def get_name(self):
        return self.__class__.__name__.replace('Pawn', '').lower()
        
        
    def get_repr(self):
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
                'name': self.get_name(),
                'initiative': initiative,
                'armor': armor,
                'actions': actions
            }
        
    def am_hq(self):
        return False
        
    def action(self, directions, name):
        found_action = NoneAction()
        log.debug('action: %s %s', directions, name)
        for direction in directions:
            log.debug(direction)
            for action in self.actions.get(direction, []):
                log.debug(action)
                if name == action.name():
                    log.debug('found')
                    if not found_action.is_defined():
                        log.debug('1')
                        found_action = action
                    else:
                        log.debug('2')
                        found_action = found_action.plus(action)
                else:
                    log.debug('not found')
                    
        return found_action

        
    def __repr__(self):
        return model_repr(self, attrs=['get_repr()'])
        
            
class HqPawn(Pawn):
    def __init__(self, army=None):
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
        
    
        
class SniperPawn(Pawn):
    def __init__(self, army):
        Pawn.__init__(self, army)
        self.is_immediate = True

        
class MoveRotatePawn(Pawn):
    def __init__(self, army=None):
        Pawn.__init__(self, army)
        self.is_immediate = True


class PushPawn(Pawn):
    def __init__(self, army=None):
        Pawn.__init__(self, army)
        self.is_immediate = True

        
class BattlePawn(Pawn):
    def __init__(self, army=None):
        Pawn.__init__(self, army)
        self.is_immediate = True


class MedicPawn(Pawn):
    def __init__(self, army=None):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True
        self.actions = {
            'A': [Heal()],
            'B': [Heal()],
            'F': [Heal()],
        }
        

class RunnerPawn(Pawn):
    def __init__(self, army=None):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True
        self.actions = {
            'A': [Melee(1)]
        }
        self.initiative = [2]
        self.is_mobile = True


class Runner2Pawn(Pawn):
    def __init__(self, army=None):
        Pawn.__init__(self, army)
        self.can_be_put_on_board = True
        self.actions = {
            'A': [Range(1)],
            'B': [Range(1)]
        }
        self.initiative = [2]
        