import fractions
import unittest

import think_bayes


class TestCookieFunction(unittest.TestCase):
    def test_bow1_given_vanilla(self):
        self.assertEqual(fractions.Fraction(3, 5), think_bayes.cookie_function('bowl1', 'vanilla'))


if __name__ == '__main__':
    unittest.main()