# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)


class Action(object):
    def __init__(self, points=None):
        self.points = points
        
    def text_repr(self):
        return ''
        
    def name(self):
        return self.__class__.__name__.replace('Action', '').lower()
        
class NullAction(Action):
    """For use inside tests
    """
    def __init__(self):
        Action.__init__(self)

        
class Melee(Action):
    def __init__(self, points):
        Action.__init__(self, points=points)
        
    def text_repr(self):
        return 's%s' % self.points
        

class Range(Action):
    def __init__(self, points):
        Action.__init__(self, points=points)

    def text_repr(self):
        return 'S%s' % self.points
        
class WhiteArmor(Action):
    def __init__(self):
        pass

    def text_repr(self):
        return 'W'
    
