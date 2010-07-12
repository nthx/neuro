# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import random
from model.ai import Strategy


class UIConsoleStrategy(Strategy):
    
    def __init__(self):
        Strategy.__init__(self)
        pass
