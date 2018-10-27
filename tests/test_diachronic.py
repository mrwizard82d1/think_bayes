"""Test the diachronic interpretation of Bayes' law:

    P(H | D) = ( P(H) * P(D | H) ) / P(D)

where:

    H is the hypothesis
    D is the data, or evidence

P(H) is also called the prior probability; that is, the probability that the hypothesis is true *before* seeing any
data. P(D | H) is the likelihood: the probability of seeing the data given the hypothesis is true. P(D) is the
normalizing constant or the probability of seeing the data under any hypothesis. Although it is different to
calculate generally, if the hypotheses are mutually exclusive and exhaustive, then P(D) is the total probability:

    P(D) = P(H-sub-1) * P(D | H-sub-1) + P(H-sub-2) * P(D | H-sub-2) + ... + P(H-sub-n) * P(D | H-sub-n)
"""

import fractions
import unittest

import think_bayes


class TestDiachronic(unittest.TestCase):

    def test_probability_bowl_1_given_vanilla(self):
        priors = {'bowl_1': fractions.Fraction(1, 2),
                  'bowl_2': fractions.Fraction(1, 2)}
        likelihoods = {('vanilla', 'bowl_1'): fractions.Fraction(3, 4),
                       ('vanilla', 'bowl_2'): fractions.Fraction(1, 2)}

        normalizing_factor = think_bayes.total_probability(['vanilla'], priors, likelihoods)
        posteriors = think_bayes.diachronic('vanilla', priors, likelihoods, normalizing_factor)

        self.assertEqual(posteriors['bowl_1'], fractions.Fraction(3, 5))

    def test_probability_bowl_2_given_vanilla(self):
        priors = {'bowl_1': fractions.Fraction(1, 2),
                  'bowl_2': fractions.Fraction(1, 2)}
        likelihoods = {('vanilla', 'bowl_1'): fractions.Fraction(3, 4),
                       ('vanilla', 'bowl_2'): fractions.Fraction(1, 2)}

        normalizing_factor = think_bayes.total_probability(['vanilla'], priors, likelihoods)
        posteriors = think_bayes.diachronic('vanilla', priors, likelihoods, normalizing_factor)

        self.assertEqual(posteriors['bowl_2'], fractions.Fraction(2, 5))

    def test_probability_bowl_1_given_chocolate(self):
        priors = {'bowl_1': fractions.Fraction(1, 2),
                  'bowl_2': fractions.Fraction(1, 2)}
        likelihoods = {('chocolate', 'bowl_1'): fractions.Fraction(1, 4),
                       ('chocolate', 'bowl_2'): fractions.Fraction(1, 2)}

        normalizing_factor = think_bayes.total_probability(['chocolate'], priors, likelihoods)
        posteriors = think_bayes.diachronic('chocolate', priors, likelihoods, normalizing_factor)

        self.assertEqual(posteriors['bowl_1'], fractions.Fraction(1, 3))

    def test_probability_bowl_2_given_chocolate(self):
        priors = {'bowl_1': fractions.Fraction(1, 2),
                  'bowl_2': fractions.Fraction(1, 2)}
        likelihoods = {('chocolate', 'bowl_1'): fractions.Fraction(1, 4),
                       ('chocolate', 'bowl_2'): fractions.Fraction(1, 2)}

        normalizing_factor = think_bayes.total_probability(['chocolate'], priors, likelihoods)
        posteriors = think_bayes.diachronic('chocolate', priors, likelihoods, normalizing_factor)

        self.assertEqual(posteriors['bowl_2'], fractions.Fraction(2, 3))

