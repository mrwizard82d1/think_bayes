"""Unit tests for the cookie problem - with eating!"""


import fractions
import unittest

import think_bayes


class TestCookieEating(unittest.TestCase):
    def test_posterior_after_construction(self):
        hypotheses = ['umbilicus', 'togae', 'satis']
        sut = think_bayes.CookieEating(hypotheses)

        self.assertEqual({'umbilicus': fractions.Fraction(1, 3),
                          'togae': fractions.Fraction(1, 3),
                          'satis': fractions.Fraction(1, 3)},
                         sut.posterior())

    def test_likelihood_vanilla_bowl1(self):
        hypotheses = ['bowl 1', 'bowl 2']
        sut = think_bayes.CookieEating(hypotheses)

        actual = sut.likelihood('vanilla', 'bowl 1')
        self.assertEqual(fractions.Fraction(3, 4), actual)

    def test_likelihood_chocolate_bowl2(self):
        hypotheses = ['bowl 1', 'bowl 2']
        sut = think_bayes.CookieEating(hypotheses)

        actual = sut.likelihood('chocolate', 'bowl 2')
        self.assertEqual(fractions.Fraction(1, 2), actual)

    def test_likelihood_after_eating_vanilla_bowl1(self):
        hypotheses = ['bowl 1', 'bowl 2']
        sut = think_bayes.CookieEating(hypotheses)

        sut.eat_cookie('vanilla', 'bowl 1')

        actual = sut.likelihood('vanilla', 'bowl 1')
        self.assertEqual(actual, fractions.Fraction(29, 39))

    def test_likelihood_after_eating_chocolate_bowl2(self):
        hypotheses = ['bowl 1', 'bowl 2']
        sut = think_bayes.CookieEating(hypotheses)

        sut.eat_cookie('chocolate', 'bowl 2')

        actual = sut.likelihood('chocolate', 'bowl 2')
        self.assertEqual(actual, fractions.Fraction(19, 39))

    def test_vanilla_bowl1(self):
        hypotheses = ['bowl 1', 'bowl 2']
        sut = think_bayes.CookieEating(hypotheses)

        sut.update('vanilla')
        sut.eat_cookie('vanilla', 'bowl 1')

        self.assertEqual({'bowl 1': fractions.Fraction(3, 5),
                          'bowl 2': fractions.Fraction(2, 5)},
                         sut.posterior())

    def test_vb1_cb2(self):
        hypotheses = ['bowl 1', 'bowl 2']
        sut = think_bayes.CookieEating(hypotheses)

        sut.update('vanilla')
        sut.eat_cookie('vanilla', 'bowl 1')
        sut.update('chocolate')

        self.assertEqual({'bowl 1': fractions.Fraction(10, 23),
                          'bowl 2': fractions.Fraction(13, 23)},
                         sut.posterior())

    def test_vb1_cb2_vb1(self):
        hypotheses = ['bowl 1', 'bowl 2']
        sut = think_bayes.CookieEating(hypotheses)

        sut.update('vanilla')
        sut.eat_cookie('vanilla', 'bowl 1')
        sut.update('chocolate')
        sut.eat_cookie('chocolate', 'bowl 2')
        sut.update('vanilla')

        self.assertEqual({'bowl 1': fractions.Fraction(29, 55),
                          'bowl 2': fractions.Fraction(26,55)},
                         sut.posterior())

