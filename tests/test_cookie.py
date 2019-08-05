import fractions
import unittest

import think_bayes


class TestCookie(unittest.TestCase):
    """Verify solutions to the cookie problem."""

    def test_probability_vanilla_from_bowl_1(self):
        """Verify that the probability of drawing the vanilla cookie from bowl 1."""
        pmf = think_bayes.Pmf()

        # Set the prior (initial) probabilities: equal probabilities of selecting from either bowl.
        pmf.set('bowl 1', 1)
        pmf.set('bowl 2', 1)

        # Multiply the prior probabilities by the likelihood of a vanilla data given a hypothesis.
        pmf.multiply('bowl 1', fractions.Fraction(3, 4))
        pmf.multiply('bowl 2', fractions.Fraction(1, 2))

        # Calculate the posterior probabilities
        pmf.normalize()

        self.assertEqual(fractions.Fraction(3, 5), pmf.probability('bowl 1'))
        self.assertEqual(fractions.Fraction(2, 5), pmf.probability('bowl 2'))

    def test_cookie_pmf_priors(self):
        """Verify the uniform prior probability of the hypotheses."""
        hypotheses = ['bowl 1', 'bowl 2']
        cookie = think_bayes.Cookie(hypotheses)

        self.assertEqual(fractions.Fraction(1, 2), cookie.probability('bowl 1'))
        self.assertEqual(fractions.Fraction(1, 2), cookie.probability('bowl 2'))

    def test_cookie_pmf_posteriors(self):
        """Verify the probability of drawing a vanilla cookie from bowl 1."""
        cookie = think_bayes.Cookie(['bowl 1', 'bowl 2'])

        # Update the Cookie based on the `Likelihood` function
        cookie.update('vanilla')

        # Assert the posterior probabilities are correct
        self.assertEqual(fractions.Fraction(3, 5), cookie.probability('bowl 1'))
        self.assertEqual(fractions.Fraction(2, 5), cookie.probability('bowl 2'))


if __name__ == '__main__':
    unittest.main()
