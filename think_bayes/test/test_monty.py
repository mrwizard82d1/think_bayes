import fractions
import unittest
import think_bayes


class TestMonty(unittest.TestCase):

    def test_monty_posterior(self):
        hypotheses = 'ABC'
        sut = think_bayes.Monty(hypotheses)
        sut.update('B')
        sut.normalize()
        posteriors = {value: mass for value, mass in sut.items()}
        self.assertEqual(posteriors['A'], fractions.Fraction(1, 3))
        self.assertEqual(posteriors['B'], 0)
        self.assertEqual(posteriors['C'], fractions.Fraction(2, 3))

    def test_monty_b_posterior(self):
        hypotheses = 'ABC'
        sut = think_bayes.MontyB(hypotheses)
        sut.update('B')
        sut.normalize()
        posteriors = {value: mass for value, mass in sut.items()}
        self.assertEqual(posteriors['A'], fractions.Fraction(1, 2))
        self.assertEqual(posteriors['B'], 0)
        self.assertEqual(posteriors['C'], fractions.Fraction(1, 2))


if __name__ == '__main__':
    unittest.main()
