"""Unit test the Pmf class."""


import fractions
import unittest

import think_bayes


class TestPmf(unittest.TestCase):
    """Define the unit tests for the Pmf class."""

    def test_set_probability_is_correct(self):
        sut = think_bayes.Pmf()
        values = range(1, 6 + 1)
        for value in values:
            sut.set(value, fractions.Fraction(1, 6))
            self.assertEqual(fractions.Fraction(1, 6), sut.probability(value))

    def test_increment_sets_mass_to_one_if_value_not_present(self):
        sut = think_bayes.Pmf()

        sut.increment('clunis')

        self.assertEqual(1, sut.probability('clunis'))

    def test_increment_sets_increases_mass_by_one_if_value_present(self):
        sut = think_bayes.Pmf()
        sut.set('praeceps', 5)

        sut.increment('praeceps')

        self.assertEqual(6, sut.probability('praeceps'))

    def test_normalize_converts_integer_masses_to_probabilities(self):
        sut = think_bayes.Pmf()
        text = 'abjecta'
        for ch in text:
            sut.increment(ch)

        sut.normalize()

        self.assertEqual(fractions.Fraction(2, 7), sut.probability('a'))
        self.assertEqual(fractions.Fraction(1, 7), sut.probability('b'))

    def test_normalize_converts_float_masses_to_probabilities(self):
        sut = think_bayes.Pmf()
        text = 'orat'
        for ch in text:
            sut.set(ch, 0.25)
        sut.increment('t')

        sut.normalize()

        self.assertEqual(0.125, sut.probability('o'))
        self.assertEqual(0.625, sut.probability('t'))

    def test_multiply_scales_probability_by_factor(self):
        sut = think_bayes.Pmf()
        sut.set('nepos', fractions.Fraction(5, 6))

        sut.multiply('nepos', 3)

        self.assertEqual(fractions.Fraction(5, 2), sut.probability('nepos'))

    def test_multiply_scales_probability_by_float_factor(self):
        sut = think_bayes.Pmf()
        sut.set('iris', 4)

        sut.multiply('iris', 0.25)

        self.assertEqual(1, sut.probability('iris'))

    def test_masses(self):
        sut = think_bayes.Pmf()
        for ch in 'pellemus':
            sut.increment(ch)

        self.assertEqual({'p': 1, 'e': 2, 'l': 2, 'm': 1, 'u': 1, 's': 1}, sut.probabilities())

    def test_probabilities(self):
        sut = think_bayes.Pmf()
        for ch in 'pellemus':
            sut.increment(ch)
        sut.normalize()

        self.assertEqual({'p': fractions.Fraction(1, 8),
                          'e': fractions.Fraction(1, 4),
                          'l': fractions.Fraction(1, 4),
                          'm': fractions.Fraction(1, 8),
                          'u': fractions.Fraction(1, 8),
                          's': fractions.Fraction(1, 8)}, sut.probabilities())

