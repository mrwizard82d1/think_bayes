"""Test the cookie problem if I eat the cookies I draw."""


import fractions
import unittest

import think_bayes


class TestCookieEating(unittest.TestCase):
    def test_vanilla(self):
        cut = think_bayes.CookieEating()

        cut.update('Vanilla')

        self.assertEqual(cut.probability('Bowl 1'), fractions.Fraction(3, 5))
        self.assertEqual(cut.probability('Bowl 2'), fractions.Fraction(2, 5))

    def test_chocolate(self):
        cut = think_bayes.CookieEating()

        cut.update('Chocolate')

        self.assertEqual(cut.probability('Bowl 1'), fractions.Fraction(1, 3))
        self.assertEqual(cut.probability('Bowl 2'), fractions.Fraction(2, 3))

    # def test_vanilla_vanilla(self):
    #     cut = think_bayes.CookieEating()
    #
    #     cut.update('Vanilla')
    #     cut.update('Vanilla')
    #
    #     self.assertEqual(cut.probability('Bowl 1'), fractions.Fraction(3, 5))
    #     self.assertEqual(cut.probability('Bowl 2'), fractions.Fraction(2, 5))
