# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)


class Action(object):
    def __init__(self, points=None):
        self.name = None
        self.points = points
        
    def text_repr(self):
        return ''
        
class NullAction(Action):
    """For use inside tests
    """
    def __init__(self):
        Action.__init__(self)
        self.name = 'null'
        
class Stab(Action):
    def __init__(self, points):
        Action.__init__(self, points=points)
        self.name = 'stab'
        
    def text_repr(self):
        return 's%s' % self.points
        

class Shot(Action):
    def __init__(self, points):
        Action.__init__(self, points=points)
        self.name = 'shot'

    def text_repr(self):
        return 'S%s' % self.points
        
class WhiteArmor(Action):
    def __init__(self):
        self.name = 'white_armor'
        pass

    def text_repr(self):
        return 'W'
    
