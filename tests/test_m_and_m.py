"""Unit tests for the M&M problem."""


import fractions
import unittest

import think_bayes


class TestMAndM(unittest.TestCase):
    def test_probability_bag1_is_1994_and_bag2_is_1996(self):
        sut = think_bayes.MAndM()

        # Update consists of two draws: 1 from bag 1 and 1 from bag 2
        sut.update(('bag1', 'yellow'))
        sut.update(('bag2', 'green'))

        self.assertEqual({'A': fractions.Fraction(20, 27),
                          'B': fractions.Fraction(7, 27)},
                         sut.posterior())
