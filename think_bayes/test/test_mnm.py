"""Test the M&M problem implemented using a Suite."""


import fractions
import unittest

import think_bayes


class TestMnm(unittest.TestCase):
    def test_yellow_1994(self):
        cut = think_bayes.MAndM('AB')
        cut.update(('bag_1', 'yellow'))
        cut.update(('bag_2', 'green'))

        self.assertEqual(cut.probability('A'), fractions.Fraction(20, 27))
        self.assertEqual(cut.probability('B'), fractions.Fraction(7, 27))
