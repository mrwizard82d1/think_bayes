import fractions
import unittest

import think_bayes


class TestCookieDiachronic(unittest.TestCase):
    def test_bowl1_vanilla(self):
        cut = think_bayes.DiachronicCookie({'bowl1': fractions.Fraction(1, 2), 'bowl2': fractions.Fraction(1, 2)},
                                           {('vanilla', 'bowl1'): fractions.Fraction(30, 40),
                                            ('vanilla', 'bowl2'): fractions.Fraction(20, 40)})
        self.assertEqual(fractions.Fraction(3, 5), cut.probability('bowl1', 'vanilla'))

    def test_bowl2_vanilla(self):
        cut = think_bayes.DiachronicCookie({'bowl1': fractions.Fraction(1, 2), 'bowl2': fractions.Fraction(1, 2)},
                                           {('vanilla', 'bowl1'): fractions.Fraction(30, 40),
                                            ('vanilla', 'bowl2'): fractions.Fraction(20, 40)})
        self.assertEqual(fractions.Fraction(2, 5), cut.probability('bowl2', 'vanilla'))

    def test_bowl1_chocolate(self):
        cut = think_bayes.DiachronicCookie({'bowl1': fractions.Fraction(1, 2), 'bowl2': fractions.Fraction(1, 2)},
                                           {('vanilla', 'bowl1'): fractions.Fraction(30, 40),
                                            ('vanilla', 'bowl2'): fractions.Fraction(20, 40),
                                            ('chocolate', 'bowl1'): fractions.Fraction(10, 40),
                                            ('chocolate', 'bowl2'): fractions.Fraction(20, 40)})
        self.assertEqual(fractions.Fraction(1, 3), cut.probability('bowl1', 'chocolate'))

    def test_bowl2_chocolate(self):
        cut = think_bayes.DiachronicCookie({'bowl1': fractions.Fraction(1, 2), 'bowl2': fractions.Fraction(1, 2)},
                                           {('vanilla', 'bowl1'): fractions.Fraction(30, 40),
                                            ('vanilla', 'bowl2'): fractions.Fraction(20, 40),
                                            ('chocolate', 'bowl1'): fractions.Fraction(10, 40),
                                            ('chocolate', 'bowl2'): fractions.Fraction(20, 40)})
        self.assertEqual(fractions.Fraction(2, 3), cut.probability('bowl2', 'chocolate'))
