"""Test the cookie problem if I eat the cookies I draw."""


import fractions
import unittest

import think_bayes


class TestCookieEating(unittest.TestCase):
    def test_vanilla_bowl1(self):
        cut = think_bayes.CookieEating()

        cut.update(think_bayes.CookieEating.vanilla_bowl_2)

        self.assertEqual(fractions.Fraction(3, 5), cut.probability('Bowl 1'))
        self.assertEqual(fractions.Fraction(2, 5), cut.probability('Bowl 2'))

    def test_vanilla_bowl2(self):
        cut = think_bayes.CookieEating()

        cut.update(think_bayes.CookieEating.vanilla_bowl_1)

        self.assertEqual(fractions.Fraction(3, 5), cut.probability('Bowl 1'))
        self.assertEqual(fractions.Fraction(2, 5), cut.probability('Bowl 2'))

    def test_chocolate_bowl1(self):
        cut = think_bayes.CookieEating()

        cut.update(think_bayes.CookieEating.chocolate_bowl_2)

        self.assertEqual(fractions.Fraction(1, 3), cut.probability('Bowl 1'))
        self.assertEqual(fractions.Fraction(2, 3), cut.probability('Bowl 2'))

    def test_chocolate_bowl2(self):
        cut = think_bayes.CookieEating()

        cut.update(think_bayes.CookieEating.chocolate_bowl_1)

        self.assertEqual(fractions.Fraction(1, 3), cut.probability('Bowl 1'))
        self.assertEqual(fractions.Fraction(2, 3), cut.probability('Bowl 2'))

    def test_vanilla_bowl1_vanilla(self):
        cut = think_bayes.CookieEating()

        cut.update(think_bayes.CookieEating.vanilla_bowl_1)
        cut.update(think_bayes.CookieEating.vanilla_bowl_1)

        self.assertEqual(cut.probability('Bowl 1'), fractions.Fraction(29, 42))
        self.assertEqual(cut.probability('Bowl 2'), fractions.Fraction(13, 42))

    def test_vanilla_bowl2_vanilla(self):
        cut = think_bayes.CookieEating()

        cut.update(think_bayes.CookieEating.vanilla_bowl_2)
        cut.update(think_bayes.CookieEating.vanilla_bowl_2)

        self.assertEqual(cut.probability('Bowl 1'), fractions.Fraction(351, 503))
        self.assertEqual(cut.probability('Bowl 2'), fractions.Fraction(152, 503))

    def test_chocolate_bowl1_chocolate(self):
        cut = think_bayes.CookieEating()

        cut.update(think_bayes.CookieEating.chocolate_bowl_1)
        cut.update(think_bayes.CookieEating.chocolate_bowl_1)

        self.assertEqual(cut.probability('Bowl 1'), fractions.Fraction(3, 16))
        self.assertEqual(cut.probability('Bowl 2'), fractions.Fraction(13, 16))

    def test_chocolate_bowl2_chocolate(self):
        cut = think_bayes.CookieEating()

        cut.update(think_bayes.CookieEating.chocolate_bowl_2)
        cut.update(think_bayes.CookieEating.chocolate_bowl_2)

        self.assertEqual(fractions.Fraction(39, 191), cut.probability('Bowl 1'))
        self.assertEqual(fractions.Fraction(152, 191), cut.probability('Bowl 2'))
