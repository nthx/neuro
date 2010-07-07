# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_soldier_a(self):
        soldier_a = SoldierAPawn(POSTERUNEK)
        
        self.assertEqual(None, soldier_a.action('A', 'melee').points)
        self.assertEqual(1, soldier_a.action('B', 'range').points)
        self.assertEqual(None, soldier_a.extra_armor)
        
        self.assertFalse(soldier_a.is_immediate)
        self.assertTrue(soldier_a.can_be_put_on_board)
        self.assertEqual([3], soldier_a.initiative)

    
    def test_01_creation_of_runner(self):
        runner = Runner()
        self.assertEqual(1, runner.action('A', 'melee').points)
        self.assertEqual(None, runner.action('A', 'range').points)
        self.assertEqual(None, runner.action('B', 'melee').points)
        self.assertEqual([2], runner.initiative)
        self.assertTrue(runner.is_mobile)
