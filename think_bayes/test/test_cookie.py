"""Test the Cookie class"""


import unittest
import fractions

import think_bayes


class TestCookie(unittest.TestCase):
    def test_bowl_vanilla(self):
        """Test the posteriors after drawing a vanilla cookie."""
        cut = think_bayes.Cookie(['Bowl 1', 'Bowl 2'])
        cut.update('Vanilla')

        self.assertEqual(cut.probability('Bowl 1'), fractions.Fraction(3, 5))
        self.assertEqual(cut.probability('Bowl 2'), fractions.Fraction(2, 5))

    def test_bowl_chocolate(self):
        """Test the posteriors after drawing a vanilla cookie."""
        cut = think_bayes.Cookie(['Bowl 1', 'Bowl 2'])
        cut.update('Chocolate')

        self.assertEqual(cut.probability('Bowl 1'), fractions.Fraction(1, 3))
        self.assertEqual(cut.probability('Bowl 2'), fractions.Fraction(2, 3))
