#!/bin/sh
#rm screenshots/* ; nosetests tests/test_board.py
rm screenshots/* ; nosetests tests/ && gqview screenshots/board-000.png 
