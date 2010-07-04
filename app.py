# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

import sys

log_format = "%(asctime)s: %(levelname)-1.1s: [%(name)s]: [%(module)s:%(funcName)s:%(lineno)d ]: %(message)s"
log_datefmt = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=log_format, datefmt=log_datefmt)

from model.board import Board



if __name__ == "__main__":
    log.debug("Heeeya!")

    board = Board()
    

