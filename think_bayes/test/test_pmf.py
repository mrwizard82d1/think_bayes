import fractions
import unittest
import think_bayes


class TestPmf(unittest.TestCase):

    def test_set_fraction(self):
        sut = think_bayes.Pmf()
        for i in range(6):
            sut.set(i, fractions.Fraction(1, 6))

        for i in range(6):
            self.assertEqual(fractions.Fraction(1, 6), sut.probability(i))


    def test_set_float(self):
        sut = think_bayes.Pmf()
        for i in range(6):
            sut.set(i, 1 / 6.0)

        for i in range(6):
            self.assertEqual(1 / 6.0, sut.probability(i))


if __name__ == '__main__':
    unittest.main()
