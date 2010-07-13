#!/bin/sh
#nosetests tests/test_player.py

#nosetests tests/test_computer_play_strategies.py
rm screenshots/* && nosetests tests/ && gqview screenshots/board-000.png 
