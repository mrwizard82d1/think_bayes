"""Test the Monty(Suite) class on the Monty Hall problem."""


import fractions
import unittest

import think_bayes


class MontyTests(unittest.TestCase):
    def test_monty_hall_random_pick_monty(self):
        cut = think_bayes.Monty('ABC')

        cut.update('B')

        self.assertEqual(cut.probability('A'), fractions.Fraction(1, 3))
        self.assertEqual(cut.probability('B'), 0)
        self.assertEqual(cut.probability('C'), fractions.Fraction(2, 3))

