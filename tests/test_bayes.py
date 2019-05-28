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

    def test_diachronic_vanilla_bowl_1(self):
        self.assertEqual(think_bayes.diachronic(self.prob_bowl_1, self.prob_vanilla_bowl_1,
                                                self.prob_vanilla_either_bowl), fractions.Fraction(3, 5))

    def test_diachronic_vanilla_bowl_2(self):
        self.assertEqual(think_bayes.diachronic(self.prob_bowl_2, self.prob_vanilla_bowl_2,
                                                self.prob_vanilla_either_bowl), fractions.Fraction(2, 5))

    def test_m_and_m_table(self):
        sut = think_bayes.Table(['A', 'B'], {'A': fractions.Fraction(1, 2), 'B': fractions.Fraction(1, 2)},
                                {'A': 20 * 20, 'B': 10 * 14})
        self.assertEqual(sut.posterior('A'), fractions.Fraction(20, 27))
        self.assertEqual(sut.posterior('B'), fractions.Fraction(7, 27))

    def test_monty_python_table(self):
        sut = think_bayes.Table('ABC', {'A': fractions.Fraction(1, 3), 'B': fractions.Fraction(1, 3),
                                        'C': fractions.Fraction(1, 3)},
                                {'A': fractions.Fraction(1, 2), 'B': 0, 'C': 1})
        self.assertEqual(sut.posterior('A'), fractions.Fraction(1, 3))
        self.assertEqual(sut.posterior('B'), 0)
        self.assertEqual(sut.posterior('C'), fractions.Fraction(2, 3))


if __name__ == '__main__':
    unittest.main()
