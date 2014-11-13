"""Defines the unit tests for the bayes_calc module."""


__author__ = 'l.jones'


import fractions
import unittest

from think_bayes import bayes_calc


class TestBayesCalc(unittest.TestCase):
    """Defines the unit tests for the bayes_calc module."""

    def test_fraction_prior_likelihood_posterior_correct(self):
        """Verify the calculation of a fractional posterior."""

        prior = fractions.Fraction(1, 3)
        likelihood = fractions.Fraction(1, 2)
        total = fractions.Fraction(1, 2)

        actual_posterior = bayes_calc.posterior(prior, likelihood, total)

        self.assertEqual(fractions.Fraction(1, 3), actual_posterior)

    def test_fraction_prior_float_likelihood_posterior_correct(self):
        """Verify the calculation of mixed posteriors."""

        prior = fractions.Fraction(1, 2)
        likelihood = 0.10 * 0.14
        total = 0.5 * 0.20 * 0.20 + 0.5 * 0.10 * 0.14

        actual_posterior = bayes_calc.posterior(prior, likelihood, total)

        self.assertAlmostEqual(7.0 / 27, actual_posterior)

    def test_float_prior_float_likelihood_posterior_correct(self):
        """Verify the calculation of the posterior."""

        prior = 0.5
        likelihood = 0.13 * 0.13
        total = 0.5 * 0.13 * 0.13 + 0.5 * 0.20 * 0.13

        actual_posterior = bayes_calc.posterior(prior, likelihood, total)
        print(actual_posterior)

        self.assertAlmostEqual(0.39, actual_posterior, places=2)
