"""Unit tests solving the cookie problem using the Pmf class."""


import fractions
import unittest

import think_bayes


class TestCookiePmf(unittest.TestCase):
    def test_bowl_1_posterior_is_correct(self):
        sut = think_bayes.Pmf()
        sut.set('bowl 1', fractions.Fraction(1, 2))
        sut.set('bowl 2', fractions.Fraction(1, 2))

        # THe likelihood of drawing vanilla from bowl 1 is 3/4.
        sut.multiply('bowl 1', fractions.Fraction(3, 4))

        # And the likelihood of drawing vanilla from bowl 2 is 1/2.
        sut.multiply('bowl 2', fractions.Fraction(1, 2))

        # But now the masses are no longer normalized so...
        sut.normalize()

        self.assertEqual(fractions.Fraction(3, 5), sut.probability('bowl 1'))

    def test_bowl_2_posterior_is_correct(self):
        sut = think_bayes.Pmf()
        sut.set('bowl 1', fractions.Fraction(1, 2))
        sut.set('bowl 2', fractions.Fraction(1, 2))

        # THe likelihood of drawing vanilla from bowl 1 is 3/4.
        sut.multiply('bowl 1', fractions.Fraction(3, 4))

        # And the likelihood of drawing vanilla from bowl 2 is 1/2.
        sut.multiply('bowl 2', fractions.Fraction(1, 2))

        # But now the masses are no longer normalized so...
        sut.normalize()

        self.assertEqual(fractions.Fraction(2, 5), sut.probability('bowl 2'))

