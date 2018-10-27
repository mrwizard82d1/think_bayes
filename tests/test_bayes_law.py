import fractions
import unittest

from .context import think_bayes


class TestBayesLaw(unittest.TestCase):

    def test_cookie(self):

        probability_bowl_1 = fractions.Fraction(1, 2)
        total_probability_vanilla = fractions.Fraction(5, 8)
        probability_vanilla_given_bowl_1 = fractions.Fraction(3, 4)
        self.assertEqual(fractions.Fraction(3, 5),
                         think_bayes.bayes_law(probability_bowl_1, probability_vanilla_given_bowl_1,
                                               total_probability_vanilla))
