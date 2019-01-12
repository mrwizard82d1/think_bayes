"""Unit tests for the Dice problem."""


import fractions
import unittest

import think_bayes


class TestDice(unittest.TestCase):
    """Defines the unit tests for the Dice problem."""

    def test_correct_priors_when_constructed(self):
        """Verify the posterior when the suite is constructed."""

        hypotheses = [4, 6, 8, 12, 20]
        sut = think_bayes.Dice(hypotheses)

        for hypothesis in hypotheses:
            self.assertEqual(fractions.Fraction(1, 5), sut.posterior()[hypothesis])

    def test_correct_posterior_when_6_observed(self):
        """Verify the posterior after observing a 6."""

        hypotheses = [4, 6, 8, 12, 20]
        sut = think_bayes.Dice(hypotheses)
        sut.update(6)

        expected = {4: 0,
                    6: fractions.Fraction(20, 51),
                    8: fractions.Fraction(5, 17),
                    12: fractions.Fraction(10, 51),
                    20: fractions.Fraction(2, 17)}
        for hypothesis, value in expected.items():
            self.assertAlmostEqual(sut.posterior()[hypothesis], float(value), 12)

    def test_correct_posterior_when_many_book_observed(self):
        """Verify the posterior after observing a many rolls."""

        hypotheses = [4, 6, 8, 12, 20]
        sut = think_bayes.Dice(hypotheses)
        for roll in [6, 8, 7, 7, 5, 4]:
            sut.update(roll)

        expected = {4: 0,
                    6: 0,
                    8: 0.91584527196901,
                    12: 0.08040342579700499,
                    20: 0.0037513022339850646}
        for hypothesis, value in expected.items():
            self.assertAlmostEqual(sut.posterior()[hypothesis], float(value), 12)

    def test_correct_posterior_when_many_code_observed(self):
        """Verify the posterior after observing a many rolls."""

        hypotheses = [4, 6, 8, 12, 20]
        sut = think_bayes.Dice(hypotheses)
        for roll in [6, 4, 8, 7, 7, 2]:
            sut.update(roll)

        expected = {4: 0,
                    6: 0,
                    8: fractions.Fraction(11390625, 12437281),
                    12: fractions.Fraction(1000000, 12437281),
                    20: fractions.Fraction(46656, 12437281)}
        for hypothesis, value in expected.items():
            self.assertEqual(sut.posterior()[hypothesis], value)
