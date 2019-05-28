# -*- coding: utf-8 -*-

from .context import think_bayes

import fractions
import unittest


class TestBayes(unittest.TestCase):

    def setUp(self):
        self.prob_bowl_1 = fractions.Fraction(1, 2)
        self.prob_bowl_2 = fractions.Fraction(1, 2)
        self.prob_vanilla_bowl_1 = fractions.Fraction(3, 4)
        self.prob_vanilla_bowl_2 = fractions.Fraction(1, 2)
        self.prob_vanilla_either_bowl = fractions.Fraction(5, 8)

    def test_smoke(self):
        self.assertEqual(2 + 2, 4)

    def test_bayes_equation_vanilla_bowl_1(self):
        self.assertEqual(think_bayes.bayes_equation(self.prob_bowl_1, self.prob_vanilla_bowl_1,
                                                    self.prob_vanilla_either_bowl), fractions.Fraction(3, 5))

    def test_bayes_equation_vanilla_bowl_2(self):
        self.assertEqual(think_bayes.bayes_equation(self.prob_bowl_2, self.prob_vanilla_bowl_2,
                                                    self.prob_vanilla_either_bowl), fractions.Fraction(2, 5))


if __name__ == '__main__':
    unittest.main()
