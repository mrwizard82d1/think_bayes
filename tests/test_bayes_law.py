import fractions
import unittest

from .context import think_bayes


class TestBayesLaw(unittest.TestCase):

    def test_vanilla_bowl_1(self):
        probability_bowl_1 = fractions.Fraction(1, 2)
        total_probability_vanilla = fractions.Fraction(5, 8)
        probability_vanilla_given_bowl_1 = fractions.Fraction(3, 4)
        self.assertEqual(fractions.Fraction(3, 5),
                         think_bayes.bayes_law(probability_bowl_1, probability_vanilla_given_bowl_1,
                                               total_probability_vanilla))

    def test_vanilla_bowl_2(self):
        probability_bowl_2 = fractions.Fraction(1, 2)
        total_probability_vanilla = fractions.Fraction(5, 8)
        probability_vanilla_given_bowl_2 = fractions.Fraction(1, 2)
        self.assertEqual(fractions.Fraction(2, 5),
                         think_bayes.bayes_law(probability_bowl_2, probability_vanilla_given_bowl_2,
                                               total_probability_vanilla))

    def test_chocolate_bowl_1(self):
        probability_bowl_1 = fractions.Fraction(1, 2)
        total_probability_chocolate = fractions.Fraction(3, 8)
        probability_chocolate_given_bowl_1 = fractions.Fraction(1, 4)
        self.assertEqual(fractions.Fraction(1, 3),
                         think_bayes.bayes_law(probability_bowl_1, probability_chocolate_given_bowl_1,
                                               total_probability_chocolate))

    def test_chocolate_bowl_2(self):
        probability_bowl_2 = fractions.Fraction(1, 2)
        total_probability_chocolate = fractions.Fraction(3, 8)
        probability_chocolate_given_bowl_2 = fractions.Fraction(1, 2)
        self.assertEqual(fractions.Fraction(2, 3),
                         think_bayes.bayes_law(probability_bowl_2, probability_chocolate_given_bowl_2,
                                               total_probability_chocolate))

