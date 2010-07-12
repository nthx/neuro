#!/bin/sh
#nosetests tests/test_sample_game.py

#nosetests tests/test_computer_play_strategies.py
nosetests tests/ && gqview screenshots/board-000.png
