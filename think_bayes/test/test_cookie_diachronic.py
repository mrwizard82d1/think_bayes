import fractions
import unittest

import think_bayes


class TestCookieDiachronic(unittest.TestCase):
    def test_bow1_vanilla(self):
        cut = think_bayes.DiachronicCookie({'bowl1': fractions.Fraction(1, 2), 'bowl2': fractions.Fraction(1, 2)},
                                           {('vanilla', 'bowl1'): fractions.Fraction(30, 40),
                                            ('vanilla', 'bowl2'): fractions.Fraction(20, 40)})
        self.assertEqual(fractions.Fraction(3, 5), cut.probability('bowl1', 'vanilla'))
