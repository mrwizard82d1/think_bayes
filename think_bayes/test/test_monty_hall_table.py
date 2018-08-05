import fractions
import unittest

import think_bayes


class TestMontyHallTable(unittest.TestCase):
    def test_random_pick_change(self):
        cut = think_bayes.MontyHallRandomPickTable()
        cut.open_door_and_no_car('B')

        self.assertEqual(fractions.Fraction(2, 3), cut.posterior('C'))

    def test_random_pick_stay(self):
        cut = think_bayes.MontyHallRandomPickTable()
        cut.open_door_and_no_car('B')

        self.assertEqual(fractions.Fraction(1, 3), cut.posterior('A'))

    def test_always_b_change(self):
        cut = think_bayes.MontyHallAlwaysBTable()
        cut.open_door_and_no_car('B')

        self.assertEqual(fractions.Fraction(1, 2), cut.posterior('C'))

    def test_always_b_stay(self):
        cut = think_bayes.MontyHallAlwaysBTable()
        cut.open_door_and_no_car('B')

        self.assertEqual(fractions.Fraction(1, 2), cut.posterior('A'))

