import fractions
import unittest

import think_bayes


class TestPmf(unittest.TestCase):
    """Defines the unit tests for the Pmf class."""

    def test_set(self):
        """Verify Pmf.set()"""
        pmf = think_bayes.Pmf()
        for value in range(6):
            pmf.set(value, fractions.Fraction(1, 6))
            self.assertEqual(fractions.Fraction(1, 6), pmf.probability(value))

    def test_increment(self):
        """Verify Pmf.increment()"""
        pmf = think_bayes.Pmf()
        raw_words = ("Four score and seven years ago, our forefathers set forth on this continent a new nation, "
                     "conceived in liberty, and dedicated to the proposition that all men are created equal.").split()
        words = [w.strip(',.') for w in raw_words]

        for value in words:
            pmf.increment(value)
        expected = {
            'Four': 1,
            'our': 1,
            'and': 2,
            'the': 1
        }
        for v, p in expected.items():
            self.assertEqual(expected[v], pmf.probability(v))

    def test_normalize(self):
        """Verify Pmf.normalize()"""

        pmf = think_bayes.Pmf()
        for x in range(6):
            pmf.set(x, x)
        pmf.normalize()
        expected = {0: 0,
                    1: fractions.Fraction(1, 15),
                    2: fractions.Fraction(2, 15),
                    3: fractions.Fraction(1, 5),
                    4: fractions.Fraction(4, 15),
                    5: fractions.Fraction(1, 3)}
        for v, p in expected.items():
            self.assertEqual(expected[v], pmf.probability(v))

    def test_multiply(self):
        """Verify Pmf.multiply()"""
        pmf = think_bayes.Pmf()
        for x in range(1, 6):
            pmf.set(x, 1)

        for x in range(1, 6):
            pmf.multiply(x, fractions.Fraction(1, x))

        for x in range(1, 6):
            self.assertEqual(fractions.Fraction(1, x), pmf.probability(x))

if __name__ == '__main__':
    unittest.main()
