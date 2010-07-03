import unittest
import datetime

import sys
import os

import logging
log = logging.getLogger(__name__)
log_format = "%(asctime)s %(levelname)-1.1s %(message)s"
log_datefmt = "%Y-%m-%d %H:%M:%S"
#basic logging configuration. Uncomment line below to see logs in console
#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=log_format, datefmt=log_datefmt)


from tests import test_board


def suite():
    return unittest.TestSuite((\
        unittest.makeSuite(test_board.Test)
    ))
    
    

if __name__ == "__main__":
    result = unittest.TextTestRunner(descriptions=1, verbosity=2).run(suite())
    sys.exit(not result.wasSuccessful())
