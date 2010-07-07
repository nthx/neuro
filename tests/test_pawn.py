# -*- coding: utf-8 -*-
from tests.base import * 

class Test(BaseTest):
    
    def test_00_creation_of_medic(self):
        medic = MedicPawn(POSTERUNEK)
        log.debug(medic)
        
        self.assertEqual(None, medic.extra_armor)
        self.assertEqual(None, medic.action('ABCDEF', 'range').points)
        self.assertEqual(None, medic.action('ABCDEF', 'melee').points)
        self.assertTrue(medic.action('A', 'heal').is_defined())
        self.assertTrue(medic.action('B', 'heal').is_defined())
        self.assertFalse(medic.action('C', 'heal').is_defined())
        self.assertTrue(medic.action('F', 'heal').is_defined())
        
        self.assertFalse(medic.is_immediate)
        self.assertTrue(medic.can_be_put_on_board)
        self.assertEqual([], medic.initiative)

    
    def test_01_creation_of_runner(self):
        runner = RunnerPawn()
        log.debug(runner)
        self.assertEqual(1, runner.action('A', 'melee').points)
        self.assertEqual(None, runner.action('A', 'range').points)
        self.assertEqual(None, runner.action('B', 'melee').points)
        self.assertEqual([2], runner.initiative)
        self.assertTrue(runner.is_mobile)

        
        runner2 = Runner2Pawn()
        self.assertEqual(2, runner2.action('ABCDEF', 'range').points)
        