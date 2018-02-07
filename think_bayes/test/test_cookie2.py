import fractions
import unittest
import think_bayes


class TestCookie2(unittest.TestCase):

    def test_vanilla_posterior(self):
        hypotheses = ['Bowl 1', 'Bowl 2']
        sut = think_bayes.Cookie(hypotheses)
        sut.update('vanilla')
        sut.normalize()
        posteriors = {value: mass for value, mass in sut.items()}
        self.assertEqual(posteriors['Bowl 1'], fractions.Fraction(3, 5))
        self.assertEqual(posteriors['Bowl 2'], fractions.Fraction(2, 5))

    def test_multiple_data_posterior(self):
        hypotheses = ['Bowl 1', 'Bowl 2']
        sut = think_bayes.Cookie(hypotheses)
        for data in ['vanilla', 'chocolate', 'vanilla']:
            sut.update(data)
        sut.normalize()
        posteriors = {value: mass for value, mass in sut.items()}
        self.assertEqual(posteriors['Bowl 1'], fractions.Fraction(9, 17))
        self.assertEqual(posteriors['Bowl 2'], fractions.Fraction(8, 17))


if __name__ == '__main__':
    unittest.main()
