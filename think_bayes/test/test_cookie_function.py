import fractions
import unittest

import think_bayes


class TestCookieFunction(unittest.TestCase):
    def test_bow1_given_vanilla(self):
        self.assertEqual(fractions.Fraction(3, 5), think_bayes.cookie_function('bowl1', 'vanilla'))

    def test_bowl2_given_vanilla(self):
        self.assertEqual(fractions.Fraction(2, 5), think_bayes.cookie_function('bowl2', 'vanilla'))

    def test_bow1_given_chocolate(self):
        self.assertEqual(fractions.Fraction(1, 3), think_bayes.cookie_function('bowl1', 'chocolate'))

    def test_bowl2_given_chocolate(self):
        self.assertEqual(fractions.Fraction(2, 3), think_bayes.cookie_function('bowl2', 'chocolate'))


if __name__ == '__main__':
    unittest.main()
