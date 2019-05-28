# -*- coding: utf-8 -*-

from .context import think_bayes

import fractions
import unittest


class TestBayes(unittest.TestCase):

    def test_smoke(self):
        self.assertEqual(2 + 2, 4)

    def test_vanilla_bowl_1(self):
        prob_cookie_from_bowl_1 = fractions.Fraction(1, 2)
        prob_vanilla_cookie_from_bowl_1 = fractions.Fraction(3, 4)
        prob_vanilla_cookie_from_either_bowl = fractions.Fraction(5, 8)
        self.assertEqual(think_bayes.bayes_equation(prob_cookie_from_bowl_1, prob_vanilla_cookie_from_bowl_1,
                                                    prob_vanilla_cookie_from_either_bowl), fractions.Fraction(3, 5))

    def test_vanilla_bowl_2(self):
        prob_cookie_from_bowl_2 = fractions.Fraction(1, 2)
        prob_vanilla_cookie_from_bowl_2 = fractions.Fraction(1, 2)
        prob_vanilla_cookie_from_either_bowl = fractions.Fraction(5, 8)
        self.assertEqual(think_bayes.bayes_equation(prob_cookie_from_bowl_2, prob_vanilla_cookie_from_bowl_2,
                                                    prob_vanilla_cookie_from_either_bowl), fractions.Fraction(2, 5))


if __name__ == '__main__':
    unittest.main()
