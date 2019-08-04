import fractions
import unittest

import think_bayes


class TestCookieManualPmf(unittest.TestCase):
    """Verify solutions to the cookie problem using a Pmf"""

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


if __name__ == '__main__':
    unittest.main()
