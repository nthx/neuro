# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

from util.text import model_repr


class Action(object):
    def __init__(self, points=None):
        self.points = points
        
    def text_repr(self):
        return ''
        
    def name(self):
        return self.__class__.__name__.replace('Action', '').lower()
        
    def is_defined(self):
        return True
        
    def __repr__(self):
        return model_repr(self, attrs=['name()'])

        
    def plus(self, action):
        self.points += action.points
        return self
        
        
class NoneAction(Action):
    """Represents sth that doesnt exist. So I dont use if action != None... inside tests
    """
    def __init__(self):
        Action.__init__(self)

    def is_defined(self):
        return False
        
        
class Melee(Action):
    def __init__(self, points):
        Action.__init__(self, points=points)
        
    def text_repr(self):
        return 'M%s' % self.points
        

class Range(Action):
    def __init__(self, points):
        Action.__init__(self, points=points)

    def text_repr(self):
        return 'R%s' % self.points
        
class WhiteArmor(Action):
    def __init__(self):
        pass

    def text_repr(self):
        return 'W'

class Heal(Action):
    def __init__(self):
        pass

    def text_repr(self):
        return 'H'
    
