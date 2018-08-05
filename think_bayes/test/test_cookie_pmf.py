"""Test the cookie problem solved using a Pmf"""


import fractions
import unittest

import think_bayes


class TestCookiePmf(unittest.TestCase):
    def test_bowl1_vanilla(self):
        cut = think_bayes.Pmf()
        cut.set('Bowl 1', fractions.Fraction(1, 2))
        cut.set('Bowl 2', fractions.Fraction(1, 2))

        cut.multiply('Bowl 1', fractions.Fraction(30, 40))
        cut.multiply('Bowl 2', fractions.Fraction(20, 40))

        cut.normalize()

        self.assertEqual(cut.probability('Bowl 1'), fractions.Fraction(3, 5))
        self.assertEqual(cut.probability('Bowl 2'), fractions.Fraction(2, 5))

    def test_bowl1_chocolate(self):
        cut = think_bayes.Pmf()
        cut.set('Bowl 1', fractions.Fraction(1, 2))
        cut.set('Bowl 2', fractions.Fraction(1, 2))

        cut.multiply('Bowl 1', fractions.Fraction(10, 40))
        cut.multiply('Bowl 2', fractions.Fraction(20, 40))

        cut.normalize()

        self.assertEqual(cut.probability('Bowl 1'), fractions.Fraction(1, 3))
        self.assertEqual(cut.probability('Bowl 2'), fractions.Fraction(2, 3))

