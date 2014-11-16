"""Defines the unit tests for the MontyPmf class."""

import fractions
import unittest

from think_bayes.monty_pmf import MontyPmfRandom, MontyPmfAlwaysB


__author__ = 'l.jones'


class TestMontyPmf(unittest.TestCase):
    """Defines the unit tests for the MontyPmf class."""

    def test_monty_picks_random(self):
        """Verify the posterior probabilities if Monty Hall picks randomly between doors that DO NOT have car."""
        # The car is behind door A, B or C.
        hypotheses = 'ABC'
        cut = MontyPmfRandom(hypotheses)

        # Monty shows door B (after you pick A)
        data = 'B'
        cut.update(data)

        expect_posterior = {'A': fractions.Fraction(1, 3), 'B': fractions.Fraction(0), 'C': fractions.Fraction(2, 3)}

        actual_posterior = dict(cut._pmf.items())

        self.assertEqual(expect_posterior, actual_posterior)

    def test_monty_picks_b(self):
        """Verify the posterior probabilities if Monty always picks door B if he can."""

        hypotheses = 'ABC'
        cut = MontyPmfAlwaysB(hypotheses)

        # Monty shows door B after you pick A.
        data = 'B'
        cut.update(data)

        expect_posterior = {'A': 0.5, 'B': 0, 'C': 0.5}

        actual_posterior = dict(cut._pmf.items())

        self.assertEqual(expect_posterior, actual_posterior)

