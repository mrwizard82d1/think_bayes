import fractions
import unittest
import think_bayes


class TestCookie(unittest.TestCase):
    def test_vanilla_posterior(self):
        actual_vanilla_posterior = think_bayes.cookie.vanilla_posterior()
        self.assertEqual(actual_vanilla_posterior, fractions.Fraction(3, 5))

if __name__ == '__main__':
    unittest.main()