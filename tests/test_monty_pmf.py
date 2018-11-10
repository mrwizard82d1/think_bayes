"""Define unit tests for the MontyPmf Hall problem using Pmf."""


import fractions
import unittest

import think_bayes


class TestMontyPmf(unittest.TestCase):
    def test_monty_hall_posterior(self):
        hypotheses = 'ABC'
        sut = think_bayes.MontyPmf(hypotheses)

        data = 'B'
        sut.update(data)

        self.assertEqual({'A': fractions.Fraction(1, 3),
                          'B': 0,
                          'C': fractions.Fraction(2, 3)}, sut.posterior())
