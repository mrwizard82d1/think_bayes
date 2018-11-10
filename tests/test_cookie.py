"""Unit tests for the Cookie class."""


import fractions
import unittest

import think_bayes


class TestCookie(unittest.TestCase):
    def test_probabilities_evenly_distributed_after_construction(self):
        sut = think_bayes.Cookie(['bowl 1', 'bowl 2'])

        self.assertEqual({'bowl 1': fractions.Fraction(1, 2),
                          'bowl 2': fractions.Fraction(1, 2)}, sut.posterior())

    def test_hypotheses_after_construction(self):
        sut = think_bayes.Cookie(['insulas', 'pudetis'])

        self.assertEqual({'insulas', 'pudetis'}, set(sut.hypotheses()))

    def test_posterior_correct_after_seeing_vanilla(self):
        sut = think_bayes.Cookie(['bowl 1', 'bowl 2'])

        sut.update('vanilla')

        self.assertEqual({'bowl 1': fractions.Fraction(3, 5),
                          'bowl 2': fractions.Fraction(2, 5)},
                         sut.posterior())

    def test_posterior_correct_after_seeing_chocolate(self):
        sut = think_bayes.Cookie(['bowl 1', 'bowl 2'])

        sut.update('chocolate')

        self.assertEqual({'bowl 1': fractions.Fraction(1, 3),
                          'bowl 2': fractions.Fraction(2, 3)},
                         sut.posterior())

