import fractions
import unittest

import think_bayes


class TestPmf(unittest.TestCase):
    def test_set(self):
        pmf = think_bayes.Pmf()
        for value in range(6):
            pmf.set(value, fractions.Fraction(1, 6))
            self.assertEqual(fractions.Fraction(1, 6), pmf.probability(value))


if __name__ == '__main__':
    unittest.main()
